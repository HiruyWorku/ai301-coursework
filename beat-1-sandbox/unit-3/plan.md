# Plan: issue #62 — Health check references `settings.redis_host`, which does not exist on Settings

## Diagnosis

`health_check()` in `api/routes/health.py` builds its Redis client as:

```python
r = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=0,
    decode_responses=True,
)
```

but `Settings` in `core/config.py` defines only `redis_url` (`redis_url: str = Field(default="redis://localhost:6379/0")`) — there is no `redis_host` or `redis_port` field anywhere on the class. Every call to `health_check()` raises `AttributeError: 'Settings' object has no attribute 'redis_host'` on the `settings.redis_host` access, before Redis is ever contacted. The surrounding `except Exception` catches this, logs `redis_health_check_failed`, and reports `"redis": "unhealthy"` — even when Redis is actually running and reachable.

Grounded in my week-2 repro (posted to the issue, quoted below): `redis-cli ping` returns `PONG` against the same running Redis container at the same time `GET /health` reports it unhealthy, and an isolated Python check outside the HTTP layer confirms `hasattr(settings, "redis_host")` is `False` while `hasattr(settings, "redis_url")` is `True`. The bug is in the attribute access, not in Redis connectivity:

> `settings` (an instance of `Settings` from `core/config.py`) has no `redis_host`/`redis_port` attributes — only `redis_url` — so `redis.Redis(host=settings.redis_host, port=settings.redis_port, ...)` in `api/routes/health.py` raises `AttributeError: 'Settings' object has no attribute 'redis_host'` on every call. ... even though Redis itself is confirmed healthy (`redis-cli ping` → `PONG`) and never actually contacted.

`pyproject.toml`'s mypy config independently confirms this is the intended, seeded defect: the `api.routes.health` override suppresses mypy's own `attr-defined` error for exactly this line, with a comment naming issue #62 by number.

## Scope

In scope: the Redis health-check call in `health_check()`, so it uses an attribute that actually exists on `Settings`.

Not in scope, explicitly deferred:
- The co-occurring Postgres failure in the same response (`"SELECT 1" should be explicitly declared as text("SELECT 1")`) — that is issue #61, a separate seeded bug in the same function, and I noted this distinction in my week-2 repro comment already. This plan does not touch the Postgres check.
- Any broader refactor of `health_check()` (e.g. splitting it into per-dependency functions, changing its response shape, or adding new dependency checks). The function's overall structure stays as-is; only the Redis client construction changes.
- Adding a `redis_host`/`redis_port` pair of settings fields as an alternative fix. redis-py's `Redis.from_url()` already parses host/port/db from a URL, so the existing `redis_url` field is sufficient and keeps one source of truth instead of two ways to configure the same thing.

## Files

- `api/routes/health.py` — the Redis client construction in `health_check()`.
- `pyproject.toml` — remove `"attr-defined"` from the `api.routes.health` mypy override's `disable_error_code` list (leaving `"call-overload"` and `"index"`, which cover the still-open #61 and any other seeded issue in that file, untouched).
- `tests/unit/test_health.py` (new file) — a regression test for the Redis branch of `health_check()`.

## Approach

1. In `api/routes/health.py`, replace the `redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, decode_responses=True)` construction with `redis.Redis.from_url(settings.redis_url, decode_responses=True)`, which parses host, port, and db directly from the existing `redis_url` setting.
2. In `pyproject.toml`, remove `"attr-defined"` from the `[[tool.mypy.overrides]]` block for `module = "api.routes.health"`, per `CONTRIBUTING.md`'s instruction that fixing a seeded bug removes its suppression entry. Leave `"call-overload"` and `"index"` in place (unrelated, still-open issues in the same file).
3. Add `tests/unit/test_health.py` with a unit test that mocks `redis.Redis.from_url` to confirm `health_check()` calls it with `settings.redis_url` and reports `"redis": "healthy"` when the mock ping succeeds, plus a case confirming a real connection failure (not an attribute error) still reports `"redis": "unhealthy"` via the same exception path.

## Test plan

Re-run my week-2 repro steps against the fix:

1. `docker compose up -d` (Postgres + Redis), confirm both `(healthy)` via `docker compose ps`.
2. `docker exec pathreview-fork-redis-1 redis-cli ping` → expect `PONG` (unchanged; Redis itself was never the problem).
3. Start the API (`uvicorn api.main:app --host 0.0.0.0 --port 8000`) and `curl http://localhost:8000/health`.
   - Before the fix (already captured in my week-2 repro comment): `HTTP_STATUS:503`, body shows `"redis":"unhealthy"`, server log shows `redis_health_check_failed error="'Settings' object has no attribute 'redis_host'"`.
   - After the fix, expected: the response's `"redis"` field reads `"healthy"`, and the server log shows no `redis_health_check_failed` line for that request. (The response may still be `503` overall because of the separate, out-of-scope `"postgres"` failure from issue #61 — the test plan's pass condition is specifically the `"redis"` field and the absence of the `AttributeError` log line, not the overall HTTP status.)
4. Re-run the isolated Python check from my week-2 repro (`hasattr(settings, "redis_host")`) — expected to still print `False` (no new field added), confirming the fix goes through `redis_url`/`from_url`, not by adding the missing attributes.
5. `make test-unit` — expect `tests/unit/test_health.py`'s new cases to pass, and the full unit suite to stay green.
6. `make typecheck` — expect no new `attr-defined` error on `api/routes/health.py` now that the real bug is fixed and its suppression is removed.

## Risks and unknowns

- `Redis.from_url()` ignores the `db=0` keyword I'm removing explicitly, but I checked both `.env.example` and `.github/workflows/ci.yml`: both set `REDIS_URL=redis://localhost:6379/0`, so the `/0` database segment is already present in every config this repo ships, and `from_url()` parses it the same way the old code's explicit `db=0` did. A repo-wide search for `redis_host`/`redis_port` found no other references outside the one buggy line, so no other code path depends on those attributes existing.
- I have not run the full `test-integration` suite locally against this change (only `test-unit` and a manual repro re-run); if an integration test asserts on the exact exception type/message from the old `AttributeError` path, it would need updating, though I found no such reference in a repo-wide search either.

## Deviations

The build matched the plan; two things worth recording honestly:

- `make typecheck` (the full-project command) fails before it reaches
  `api/`: `numpy/__init__.pyi:737: error: Type statement is only
  supported in Python 3.12 and greater`. I confirmed this is
  pre-existing and unrelated to this change by stashing my commit and
  running the same command against `main` at `f89c06f` — identical
  failure, same file, same line. It's a mismatch between this local
  environment's installed numpy stubs and mypy's parsing, not
  something #62's fix touches. The plan's test-plan step 6 ("no new
  `attr-defined` error on `api/routes/health.py`") is still verified:
  `mypy api/routes/health.py` run directly (bypassing the broken
  project-wide walk) reports "Success: no issues found in 1 source
  file."
- The test file (`tests/unit/test_health.py`) needed a small lint fix
  after writing it: `ruff` flagged nested `with` statements (SIM117)
  in one test, and `black` reformatted the file. Both were caught and
  fixed by the repo's own pre-commit hooks before the commit landed;
  no change to the approach or the test's actual assertions.

Nothing about the diagnosis, scope, approach, or files changed from
what's written above.
(filled in after the build)
