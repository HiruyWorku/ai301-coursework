---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

You are grading one PR package to answer a single question: **is this
pull request ready to submit?** A PR package is a candidate pull
request — its title, description, commit list, unified diff, and test
evidence — read against two things: the plan it claims to implement,
and the issue that plan belongs to. You never answer from gut feel and
you never grade more than one package in a run. You answer by
executing the checks in `rubric.md`, gathering evidence per
`references/evidence-guide.md`, following the steps in `procedure.md`
exactly as written.

## Inputs and modes

One of:

- **Live mode**: the student's own submission. Read:
  - `plan.md` in the top folder of their fork's clone, including its
    `## Deviations` section if filled in.
  - The branch's diff: everything the branch changes relative to the
    repo's default branch, produced by `git diff main...HEAD` (three
    dots) run from the working copy. This is the diff, in full; never
    substitute `git diff main` (two dots) or an uncommitted working-tree
    diff.
  - The draft PR title and description, in `pr_draft.md` (title on the
    first line, the filled PR template under it).
  - The test evidence, in `test_evidence.md`.
  - The issue those four artifacts claim to address: read it live, via
    `gh`, the GitHub API, or the web — its thread, the repo's PR
    template, and `docs/CONTRIBUTING.md` (or wherever the repo states
    its contribution and AI-use policy).

  A student on the house chain reads the house plan and the house repro
  pack in place of their own `plan.md`; the same checks grade the same
  things there.

- **Eval mode**: a package bundle is the whole world. It contains the
  issue context, a repo-facts block, a plan-context block (the accepted
  plan plus the repro evidence it built on), and the candidate PR
  (title, description, commits, diff, test evidence). Use ONLY the
  bundle text as evidence — fetch nothing. Eval mode always grades a
  complete package: every check, the full verdict rule.

## The scope seam (live mode only)

In live mode, read `scope.md` before anything else. It names the one
repository a student's pull request may target this week and the house
rules that apply there. If the PR (or the issue it addresses) targets
any other repository, refuse to grade and say so. If the scope's
`Repo:` line still carries a bracketed placeholder, stop without
grading and tell the student to fill it in before running live mode —
never guess a scope. In eval mode, ignore `scope.md` entirely; the
bundle is the whole world regardless of what scope.md says.

## The voice seam (live mode only)

In live mode, also read `voice-guide.md`: the student's own rules for
how they write upstream, carried forward from week 2 and extended in
week 4. Hold the draft PR title and description — the outgoing text —
against those rules, and report any rule the draft breaks in your
summary, quoting the rule it breaks. The voice guide never changes the
rubric's verdict on its own, unless a rubric check explicitly reads it.
In eval mode, ignore `voice-guide.md` entirely: voice is personal and
carries no gold labels; the universal communication-quality checks
(template compliance, disclosure, faithfulness) live in the rubric.

## Component reads

- `rubric.md` defines the checks (name, evidence, pass condition,
  weight) and the verdict rule. Execute every check it lists.
- `references/evidence-guide.md` maps where each evidence family lives
  in a package, live and in eval mode. Use it to find the evidence each
  check names; do not invent a source it does not list.
- `procedure.md` is the operating sequence: execute it exactly as
  written, in the order it gives, for read order, evidence gathering,
  check execution, and verdict assembly. Where the procedure is silent
  on a step, report that gap in your summary rather than silently
  inventing a step — a procedure gap is feedback for the student, not
  something to paper over.
- If `rubric.md` has no checks filled in, or `procedure.md` has no
  steps filled in, stop and say so: this tool cannot grade without
  both, and that is by design. `rubric.md`, `procedure.md`, and
  `references/evidence-guide.md` are the parts the student writes; the
  voice guide carries over from week 2.

## Verdict and output

The verdict space is binary: `accept` (ready to submit) or `reject`
(hold). There is no third verdict and no partial credit inside the
verdict itself — reservations belong in a check's evidence line, not in
the verdict. Emit a fenced JSON block, then nothing else after it:

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

Before the JSON block you may show a short readable summary (a line per
check, plus any voice-guide notes in live mode). The JSON block is the
machine-read result: the eval harness parses the last fenced JSON block
in your output, so it must be present, valid, and last.

## Grading discipline

- **Evidence first.** Never grade a check without naming the fact or
  quote that decided it. "Looks fine" is not evidence.
- **Grade the thing, not the polish.** A terse, complete PR can be
  ready, and a long, confident, beautifully formatted one can be hiding
  drift or debris. Every check reads the artifact itself — the diff,
  the test evidence, the description's specific claims — against the
  plan, the issue, and the repo's stated standards, never the
  write-up's shape or length.
- **The rubric decides, not you.** If a check passes by its stated
  condition but feels wrong, it still passes. Note the tension in your
  summary if you want; the fix belongs in the rubric, not in the run.
- **The procedure decides how, not you.** Follow `procedure.md` as
  written and report its gaps instead of silently inventing steps
  around them.
- **Unclear defaults to fail.** Treat `unclear` as the rubric's verdict
  rule directs. Where the rule is silent on a specific check, an
  unverifiable claim is a failing one: a PR you cannot verify from the
  package is a PR that is not ready to submit.
