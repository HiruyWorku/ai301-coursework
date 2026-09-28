# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

Record of your claim and reproduction on the issue you chose in Unit 1, and of the
evaluation runs that produced `eval-run.txt`. This file is graded at the path above; a copy
kept anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your identity upstream

**GitHub username**

HiruyWorku

---

## Posted upstream

**Claim comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62#issuecomment-5861147308

Hi! I'd like to investigate issue #62 as a first contribution here. The health check's Redis probe in `api/routes/health.py` calls out to `settings.redis_host`/`settings.redis_port`, and `Settings` in `core/config.py` doesn't define those fields — I want to confirm exactly how that fails locally (and whether the surrounding exception handling masks it) before looking at a fix. I'll set up the dev environment and report back with what I find.

**Reproduction comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62#issuecomment-5861207338

Environment: PathReview at commit `f89c06f` (fork `HiruyWorku/pathreview-ai301-fa26-s1`), Python 3.14.6, FastAPI 0.141.1, SQLAlchemy 2.1.1, redis-py 8.1.0, macOS 25.5.0 (arm64, Darwin). Backing services via `docker compose up -d` (`postgres:16-alpine`, `redis:7-alpine`), app run with `uvicorn api.main:app --host 0.0.0.0 --port 8000` (no `--reload`).

Steps:

```
$ docker compose up -d
$ docker compose ps
# db and redis both "Up ... (healthy)"
$ docker exec pathreview-fork-redis-1 redis-cli ping
PONG
$ source .venv/bin/activate && uvicorn api.main:app --host 0.0.0.0 --port 8000 &
$ curl -s -o /tmp/health-response.json -w "HTTP_STATUS:%{http_code}\n" http://localhost:8000/health
```

Response:

```
HTTP_STATUS:503
{"detail":{"status":"unhealthy","dependencies":{"postgres":"unhealthy","redis":"unhealthy","vector_db":"healthy"},"safety_events_last_hour":0,"timestamp":"2026-09-28T00:18:04.036683"}}
```

Server log for that request:

```
2026-09-27 20:18:04 [error] postgres_health_check_failed error="Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')" request_id=d613e41a-5670-414a-93e1-5dc0943f4fd7
2026-09-27 20:18:04 [error] redis_health_check_failed error="'Settings' object has no attribute 'redis_host'" request_id=d613e41a-5670-414a-93e1-5dc0943f4fd7
```

Isolating the redis path directly, without going through the HTTP layer at all:

```
$ python -c "
from core.config import settings
print('has redis_host:', hasattr(settings, 'redis_host'))
print('has redis_port:', hasattr(settings, 'redis_port'))
print('has redis_url:', hasattr(settings, 'redis_url'), '->', settings.redis_url)
try:
    settings.redis_host
except AttributeError as e:
    print('AttributeError:', e)
"
has redis_host: False
has redis_port: False
has redis_url: True -> redis://localhost:6379/0
AttributeError: 'Settings' object has no attribute 'redis_host'
```

Expected: with Redis actually running and reachable, `GET /health` should report `"redis": "healthy"`.

Actual: `settings` (an instance of `Settings` from `core/config.py`) has no `redis_host`/`redis_port` attributes — only `redis_url` — so `redis.Redis(host=settings.redis_host, port=settings.redis_port, ...)` in `api/routes/health.py` raises `AttributeError: 'Settings' object has no attribute 'redis_host'` on every call. The surrounding `except Exception` in `health_check()` catches this, logs it, and reports `"redis": "unhealthy"`, even though Redis itself is confirmed healthy (`redis-cli ping` → `PONG`) and never actually contacted.

Note: the same response also shows `"postgres": "unhealthy"`, but that is a separate, unrelated defect (issue #61 — a raw `"SELECT 1"` string used where SQLAlchemy 2.x requires `text("SELECT 1")`) that happens to live in the same `health_check()` function. It is not part of this reproduction and I haven't investigated it further here.

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. `--only pkg-02,pkg-04,pkg-06,pkg-08,pkg-16,pkg-17,pkg-19,pkg-20` (the 8 trickiest edge
   cases, chosen up front to smoke-test the checks designed for exactly these failure
   modes): 8/8.
2. `--only pkg-01,pkg-03,pkg-05,pkg-07,pkg-09,pkg-10,pkg-11,pkg-12,pkg-13,pkg-14,pkg-15,pkg-18`
   (the remaining 12): 9/12 — pkg-01, pkg-05, and pkg-12 wrongly rejected, on "Version or
   build delta is acknowledged" and "Steps are followable by a stranger."
3. `--only pkg-01,pkg-05,pkg-12,pkg-16,pkg-06,pkg-18` after loosening both checks (the
   first three are the fixes; pkg-16, pkg-06, pkg-18 are canaries re-run to confirm the
   loosened checks still correctly reject the packages they exist to catch): 6/6.
4. Full run, 20 items, not saved: 20/20 (bar: PASS, all 5 category floors met).
5. Full run, 20 items, `--save-run eval-run.txt`: **20/20** (bar: PASS, all 5 category
   floors met). This is the run committed in `eval-run.txt`.

**Package analysis**

`pkg-01` (httpie/cli#1640, missing `Content-Type` header). Gold label: `accept`
("faithful offline repro of the missing Content-Type with a control run; env recorded;
claim specific and modest"). Under run 2's rubric wording, my rubric's decision was
`reject`, failed on "Version or build delta is acknowledged."

The issue itself states no target version at all — it's a bare bug report with no
"Version:" field. But the thread has a commenter theorizing the bug is "a regression in
multidict 6.5.0" that "has since shipped upstream," and the candidate's repro report
names `multidict 6.6.0` in its environment line without discussing that thread comment.
My check's evidence at that point was just "the report's version vs. whatever version(s)
the issue... confirms the bug on," with no restriction on *whose* stated version counts —
so the grading model treated a different commenter's speculative theory about an
unrelated dependency as "the version the issue confirms," and failed the package for not
addressing it. After narrowing the check to compare only against a version the issue's
own reporter explicitly states (and treating "the issue names no version at all" as
nothing to deviate from), pkg-01 correctly reads as `accept` in every run since — there
is no reporter-stated version to have silently drifted from.

**Check rationale**

The "Version or build delta is acknowledged" check's evidence column, quoted from the
uploaded `rubric.md`:

> The repro report's stated version/build, compared against whatever version(s) the
> issue's own reporter explicitly states or confirms the bug on (a "Version:" field, an
> environment block, or explicit "confirmed on X" wording in the issue body itself — not
> a version number a different commenter merely speculates is related).

And its pass condition:

> Passes if the report's version matches what the issue's reporter states, if the issue
> names no specific version at all (nothing to deviate from), or if the report's version
> differs from the reporter's and the report explicitly names that difference. Fails only
> if the issue's reporter explicitly states an affected version, the report silently uses
> a different one, and the report never mentions the difference.

It reads this way because of pkg-01: an earlier wording just said "compared against
whatever version(s) the issue... confirms the bug on," with no restriction on whose
statement counts as a confirmed version. That let a commenter's unrelated speculation
about a dependency's version stand in for "the version the issue confirms," which wrongly
failed an otherwise-clean report for not addressing a theory nobody actually established.
I rejected leaving the check's target implicit and named it explicitly: only the issue's
own reporter's stated version is the baseline a report can silently drift from; a
different commenter's guess about root cause is not.

**Trade-offs**

Narrowing the check to only the issue reporter's own stated version trades away a case it
used to (accidentally) catch: a maintainer commenting later in the thread that the bug is
now fixed as of some version, or that reproduction should happen on a specific newer
build, is no longer a baseline a report can silently drift from — only the original
report's stated version is. A candidate who silently reproduces on a version a maintainer
has since flagged as irrelevant, while ignoring that maintainer comment entirely, would
now pass this check. To confirm the narrowing didn't reopen the case it was built to
catch, I re-ran pkg-16 (silent stale-version reproduction, where the *reporter's own*
template checkboxes confirm the bug on latest and main) as a canary after the change: it
still correctly rejects, since that deviation is against the reporter's own statement, not
a bystander's guess.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/repro-check/`.
