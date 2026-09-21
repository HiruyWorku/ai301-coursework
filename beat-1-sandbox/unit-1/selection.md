# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62

**Verdict output**

`````
## Grading summary

**Scope check:** All three URLs are in `codepath/pathreview-ai301-fa26-s1` — in scope. Path Review house rule applies (claim comments from classmates don't block a claim), though none of these three actually have any comments.

**Repo-level facts (shared by all three):** not archived, last push 2026-09-16 (4 days ago) — both required repo-health checks pass for every candidate. `docs/CONTRIBUTING.md` states no AI-contribution ban (it actually documents an AI-assisted workflow: removing seeded `xfail` markers, etc.) — contribution-policy check passes for all three. I sampled comments on 8 other issues (65–71, 73) and found zero owner/member first-responses — only student claim comments — so the *preferred* maintainer-responsiveness check fails/unclear across the board (doesn't affect verdicts, and doesn't differentiate ranking since it's equal for all three).

### Issue #72 — `verify_password` raises `UnknownHashError`
| Check | Grade | Evidence |
|---|---|---|
| Not archived | pass | `isArchived: false` |
| Recent repo activity | pass | last push 2026-09-16 |
| Bounded scope | pass | Names exact files (`core/security.py`, `tests/unit/test_security.py`), one diagnosed cause, one fix, estimated 1–2h |
| Unclaimed | pass | `assignees: []`, 0 comments, no PRs anywhere in repo |
| AI-contribution policy | pass | No ban in CONTRIBUTING.md |
| Maintainer responsiveness (pref) | fail | No owner/member reply in sample |
| Well-specified fix (pref) | pass | Exact files + diagnosed cause named |

**Verdict: accept**

### Issue #62 — health check references nonexistent `settings.redis_host`
| Check | Grade | Evidence |
|---|---|---|
| Not archived | pass | same as above |
| Recent repo activity | pass | same as above |
| Bounded scope | pass | Names files (`api/routes/health.py`, `core/config.py`), diagnosed root cause (`redis_host`/`redis_port` don't exist, should use `redis_url`), one fix |
| Unclaimed | pass | `assignees: []`, 0 comments, no PRs |
| AI-contribution policy | pass | same as above |
| Maintainer responsiveness (pref) | fail | same as above |
| Well-specified fix (pref) | pass | Root cause and fields explicitly diagnosed |

**Verdict: accept**

### Issue #61 — health check DB probe passes raw SQL string
| Check | Grade | Evidence |
|---|---|---|
| Not archived | pass | same as above |
| Recent repo activity | pass | same as above |
| Bounded scope | pass | Single file (`api/routes/health.py`), diagnosed cause (SQLAlchemy 2.x requires `text()`), one fix |
| Unclaimed | pass | `assignees: []`, 0 comments, no PRs |
| AI-contribution policy | pass | same as above |
| Maintainer responsiveness (pref) | fail | same as above |
| Well-specified fix (pref) | pass | Exact error and fix named |

**Verdict: accept**

## Ranked read-out (fit: Python/backend comfort, wants larger-codebase navigation practice, wants to avoid frontend/CSS and niche domain knowledge like crypto)

1. **#62** — best fit: it's a Python/FastAPI backend bug that requires reading across two files (`api/routes/health.py` and the `Settings` model in `core/config.py`) to connect the mismatch, which is good practice for navigating an unfamiliar codebase, with zero niche domain knowledge required.
2. **#61** — equally clean and well-specified, single-file SQLAlchemy fix; ranks just below #62 only because it's a narrower one-file change with less codebase-navigation practice.
3. **#72** — otherwise identical quality, but it sits in the password-hashing module; nothing here requires actual cryptography expertise (it's exception-handling around a library call), but it's adjacent to the "niche domain knowledge" area you said you'd rather avoid, so it ranks last among three equally-valid accepts.

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/62",
    "checks": [
      {"name": "Not archived", "grade": "pass", "evidence": "isArchived: false"},
      {"name": "Recent repo activity", "grade": "pass", "evidence": "last push 2026-09-16, 4 days before today (2026-09-20)"},
      {"name": "Bounded scope", "grade": "pass", "evidence": "Body names exact files and root cause: Settings lacks redis_host/redis_port, probe should use redis_url"},
      {"name": "Unclaimed", "grade": "pass", "evidence": "assignees: [], comments: [], no PRs found repo-wide"},
      {"name": "Contribution policy allows AI-assisted work", "grade": "pass", "evidence": "docs/CONTRIBUTING.md documents an AI-assisted workflow, no ban"},
      {"name": "Maintainer responsiveness", "grade": "fail", "evidence": "No owner/member comment found across 8 sampled issues"},
      {"name": "Well-specified fix", "grade": "pass", "evidence": "Body names exact fields and the fix (use redis_url)"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/61",
    "checks": [
      {"name": "Not archived", "grade": "pass", "evidence": "isArchived: false"},
      {"name": "Recent repo activity", "grade": "pass", "evidence": "last push 2026-09-16, 4 days before today (2026-09-20)"},
      {"name": "Bounded scope", "grade": "pass", "evidence": "Body names exact file and cause: raw 'SELECT 1' string needs sqlalchemy.text() under SQLAlchemy 2.x"},
      {"name": "Unclaimed", "grade": "pass", "evidence": "assignees: [], comments: [], no PRs found repo-wide"},
      {"name": "Contribution policy allows AI-assisted work", "grade": "pass", "evidence": "docs/CONTRIBUTING.md documents an AI-assisted workflow, no ban"},
      {"name": "Maintainer responsiveness", "grade": "fail", "evidence": "No owner/member comment found across 8 sampled issues"},
      {"name": "Well-specified fix", "grade": "pass", "evidence": "Exact error message and fix named in body"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/72",
    "checks": [
      {"name": "Not archived", "grade": "pass", "evidence": "isArchived: false"},
      {"name": "Recent repo activity", "grade": "pass", "evidence": "last push 2026-09-16, 4 days before today (2026-09-20)"},
      {"name": "Bounded scope", "grade": "pass", "evidence": "Body names exact files, diagnosed cause (UnknownHashError escapes), one fix, estimated 1-2h"},
      {"name": "Unclaimed", "grade": "pass", "evidence": "assignees: [], comments: [], no PRs found repo-wide"},
      {"name": "Contribution policy allows AI-assisted work", "grade": "pass", "evidence": "docs/CONTRIBUTING.md documents an AI-assisted workflow, no ban"},
      {"name": "Maintainer responsiveness", "grade": "fail", "evidence": "No owner/member comment found across 8 sampled issues"},
      {"name": "Well-specified fix", "grade": "pass", "evidence": "Exact files and diagnosed cause named in body"}
    ],
    "verdict": "accept"
  }
]
```
`````

---

## Eval iterations

Quote source text directly in each field below. Paraphrase does not satisfy them.

**Run history**

1. `--limit 2` smoke test (issue-01, issue-02): 1/2 — issue-01 (a docs task with several
   update steps) was wrongly failed on "Bounded scope."
2. `--only issue-01,issue-05,issue-10` after loosening "Bounded scope" to distinguish a
   single multi-step task from a true umbrella: 3/3.
3. `--only issue-03,issue-08,issue-12,issue-13,issue-15,issue-17,issue-18,issue-20`:
   9/9.
4. `--only issue-04,issue-06,issue-07,issue-11,issue-14,issue-16,issue-19`: 6/7 —
   issue-19 (a bug with two diagnosed causes and three suggested approaches) was wrongly
   failed on "Bounded scope."
5. `--only issue-19,issue-01,issue-05,issue-10` after refining "Bounded scope" again
   (diagnosis/menu-of-approaches for one fix is not an umbrella; only a checklist framed
   for separate contributors is): 4/4, no regression on the earlier umbrella cases.
6. Full run, 20 items, not saved: 19/20 (bar: PASS) — issue-15 graded `accept` against a
   `reject` gold label.
7. Full run, 20 items, `--save-run eval-run.txt`: **20/20** (bar: PASS, all 5 category
   floors met). This is the run committed in `eval-run.txt`.

**Issue analysis**

`issue-19` (zxcalc/zxlive#517, "Selecting large subgraphs in proof mode freezes the
UI"). Gold label: `accept` ("maintainer-diagnosed performance bug with named causes,
unclaimed"). Under run 4's rubric wording, my rubric's decision was `reject`, failed on
"Bounded scope."

The issue body lists two numbered "potential causes" and three numbered "additional
suggestions" (multi-processing, selective matching, threading the rewrite). My
"Bounded scope" check at that point read any numbered list in an issue body as a
signal of an umbrella/checklist issue — the same pattern that correctly rejects
issue-05 and issue-10, which really are checklists meant to be split across
contributors. It didn't yet distinguish that shape from a maintainer diagnosing one
bug and sketching several ways someone could fix it: still one contributor, one PR,
one symptom. After rewording the check (run 5) to fail only when the list items are
"separable pieces of work the issue itself frames as being claimed and shipped
independently," issue-19 correctly reads as one bounded bug and the rubric's decision
matches the gold label (`accept`) in every run since.

**Check rationale**

The "Bounded scope" check's pass condition, quoted from the uploaded `rubric.md`:

> Passes even when the single requested change has several concrete steps, edits
> several files, updates several docs pages, or (for a bug) names several candidate
> causes and several possible fix approaches for that one symptom — none of that is an
> umbrella, because it is still one contributor delivering one fix or one feature in
> one PR. Only fail on a numbered/checklist body when the items are separable pieces of
> work the issue itself frames as being claimed and shipped independently (different
> sub-tasks for different contributors/PRs), not when the numbers are just a diagnosis
> or a menu of implementation options for a single change.

It's written this way because "an issue with a numbered list is an umbrella" is the
kind of shortcut that reads structure instead of intent, and it fails in both
directions: issue-01 (one docs task broken into concrete update steps) and issue-19
(one bug with diagnosed causes and candidate fixes) both have numbered lists but are
each one contributor's bounded PR, while issue-05 and issue-10 are checklists the issue
text itself invites different people to split. The check now asks what the list is
*for* — one change with several parts, versus several changes for several people —
rather than whether a list exists at all.

**Trade-offs**

Loosening the check from "any numbered list fails" to "only a list framed for separate
contributors fails" trades a hard, easy-to-apply structural signal for a judgment call
about intent, which is harder for another grader to reproduce identically. The case it
now accepts that the earlier, stricter wording would have (correctly, for the eval set)
rejected: an issue that lists several plausible fixes for one symptom without any
maintainer ever picking one ("could do A, B, or C") could now pass "Bounded scope" even
though the actual shape of the fix isn't settled — the check leans on the separate
"maintainer-endorsed spec" clause to catch that, but a vague multi-option bug report
with no maintainer comment at all is a case this check could still wrongly accept. To
confirm the loosened wording didn't reopen the umbrella cases it exists to catch, I
re-ran the two true umbrellas as canaries with `--only issue-05,issue-10` (run 5) after
the change: both still correctly reject.

---

## Selection rationale

Graded on whether all three are answered, in your own words. Not on how good the
reasoning is, and not on length — a short honest answer to each earns the full marks.
This is also the basis for the claim comment you write in Unit 2.

**Selection rationale**

1. Issue #62 is a Python/FastAPI backend bug — my strongest language — and it's small
   enough for the time I have this week: the fix is naming the right `Settings` field
   in one config file and using it in one health-check route. It also forces me to read
   two files to connect the symptom to the cause, which is exactly the
   "navigate an unfamiliar codebase" practice I said I wanted, without drifting into
   frontend/CSS work or a domain (crypto, parsing internals) I don't know yet.
2. The verdict correctly identified that the repo is alive, the issue is unclaimed, the
   fix is concretely scoped (exact fields and files named), and the contribution policy
   doesn't block AI-assisted work — all things I could check myself but that the rubric
   made me check explicitly rather than assume. What the rubric can't weigh is how *I*
   feel about the three accepted candidates: #61 and #72 were equally valid accepts, and
   I picked #62 over the single-file #61 specifically because tracing a bug across two
   files felt like more useful practice than a one-line fix, and over #72 because
   password-hashing code felt closer to "niche domain" territory even though the actual
   fix there is just an exception handler.
3. I expect claiming it to be low-difficulty: it's unclaimed with zero comments, the
   repo is a shared classroom fork so the house rule means even a stray claim comment
   from a classmate wouldn't block me, and the fix itself doesn't depend on any
   in-progress design decision or another person's PR landing first. The main risk is
   collision with another student claiming the same issue around the same time, which
   the house rule already treats as a non-issue for credit.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
