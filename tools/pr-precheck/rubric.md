# Rubric: is this pull request ready to submit?

<!--
THIS IS THE PART YOU WRITE (fourth week running; this is the rubric's
final form in the sandbox). Your frame in SKILL.md executes whatever
checks you define here, via your procedure.md. It ships empty on
purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the diff read against the plan's scope, the test
     evidence read against the plan's test plan, the description read
     against the diff, the repo-facts block's template asks) or a
     location from your references/evidence-guide.md. "The PR" is not
     a source; "the diff's changed files read against the plan's
     stated boundary" is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself
     (does the diff fall inside the plan plus its deviation notes? is
     the claimed evidence observable?), never the write-up's shape
     (how long the description is, how many commits there are).
     Structure-shaped checks are what make graders disagree with
     themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (submit) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. State the `unclear`
   treatment explicitly: the frame here is YOUR SKILL.md, so a rubric
   that stays silent is only covered if your frame's grading
   discipline says what happens (the contract's own default is that
   an unverifiable claim fails).

Cover what actually gets bad PRs submitted. The failure families the
lecture named ARE the harness's scoring categories, same names as the
eval README: silent drift (the diff silently does more or less than
the posted plan, or the description claims fidelity the diff
contradicts), not tested (the evidence proves nothing observable, or
the repo's own checks were never run), unreviewable (debris or
unrelated hunks bury the change), and standards wall (the repo's
stated template and disclosure asks are ignored). Your evidence
guide's four headings map onto these one to one (plan fidelity =
silent drift, test evidence = not tested, diff quality =
unreviewable, standards and comms = standards wall), and the category
floor is scored on exactly these names plus clear accept. A rubric
that ignores a category will fail the eval packages built around
that category. And remember the honest-outcome
rule, fourth week running: a PR that honestly discloses a shortfall
can be ready; a rubric that equates "less than everything" with
"hold" fails the set.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Diff matches the plan's scope, or deviations are noted | The diff's changed files and their content, read against the plan's stated scope/boundary/Files section and, if present, its `## Deviations` note. | Passes if every change in the diff falls inside the plan's stated scope, OR any change outside that scope (extra work, or a promised item the plan scoped in that the diff omits) is explicitly named in a deviation note. Fails if the diff contains a change beyond the plan's stated scope with no deviation note covering it, or omits something the plan's scope promised with no deviation note explaining why — in either direction, silently. An item the plan itself already named as "not in scope" from the start is not a shortfall; only promised-then-missing, or unpromised-then-present, counts. | required |
| Description's fidelity claims match the diff | Specific claims in the PR description about what the change does or does not do (e.g. "implements the plan exactly," "no changes beyond it," "X now does Y"), read against the diff's actual content. | Passes if every such claim is substantively true of the diff — including a reasonable paraphrase of implementation detail that doesn't change what a reviewer would conclude about scope or behavior (e.g. "one function touched" when one existing function's logic changed and a small helper was factored out to implement that same change, not a second independent change; "tests added for X and Y" when the added tests substantively exercise those cases even if not phrased identically). Fails when a claim overstates what the diff delivers (a described behavior, file, or test case that is simply not present), understates it (an unrelated or larger change than described, e.g. an entire extra file or feature the description never mentions), or when the gap between the claim and the diff would change a reviewer's picture of what the PR actually does. | required |
| Test evidence is decisive and complete | The PR's test-evidence section, read against every distinct failure mode the plan's test plan names as something the fix must resolve, any separate regression/unchanged-behavior controls, and the repo's own stated checks (lint, typecheck, unit tests, integration tests, or whatever the repo's PR template/docs ask for). | Passes if every distinct failure mode the plan names (not merely one of several, when the plan names more than one) is backed by one of two things: real, specific manual before/after facts (exact output, an exact returned value/exit code/error, or an exact count or state change) using the same trigger conditions the plan specified, not an adjacent, easier, or already-working case; OR a new automated test present in the diff whose name and assertions directly verify that specific scenario, combined with a real, specific report that the suite containing it passes (a count, not a bare "passes"). Either form is sufficient; a scenario doesn't need both. Separate regression/unchanged-behavior controls need the same concreteness as the primary failure mode (a specific returned value, a specific "no diff"/"unchanged" confirmation tied to a real comparison — not a bare adjective), because a control is standing in for evidence about actual behavior. Repo-required checks (lint, typecheck, a CI/build command, a whole-suite test run) are different: naming the command and stating its result (passed, or named command names X failures) is sufficient on its own — "`go test ./...` passes" or "fmt and clippy clean" is a normal, adequate report for a repo-wide check precisely because it is secondary confirmation alongside an already-decisive primary repro, not a substitute for one. A comment-style before/after annotation on the primary failure mode still passes when the annotated values themselves are specific and concrete (exact error text, exact exit code, exact return value); it fails when the comment asserts a match or success ("matches expected output," "now works") without showing the value itself. Fails if any plan-named failure mode is missing, run against the wrong trigger condition, backed only by a vague assertion with no specific fact attached, or if a regression control is asserted with zero specifics; a bare "passes" fails ONLY when it is standing in for the primary failure mode itself (the actual not-tested pattern), never when it is a named repo-wide check reported alongside solid primary evidence. | required |
| Diff is free of debris | The unified diff's hunks and the commit list. | Passes if the diff contains only the content that implements the plan's change: no debug print/log statements left in, no commented-out code (an abandoned attempt or a stale line), no dead/unused functions or variables, no pure formatting/re-indent churn unrelated to the fix, no import reordering or restructuring the fix doesn't require. Fails if any one of these debris types is present anywhere in the diff, however correct and well-evidenced the actual fix is — debris sinks an otherwise-ready PR on its own. | required |
| PR meets the repo's stated template, policy, and thread direction | The repo-facts block's PR-template asks and stated contribution/AI-use policy, and the thread highlights for any explicit maintainer direction, read against the PR description and its approach. | Passes if every section the repo's PR template requires is present with real, specific content (not an empty checkbox or boilerplate restating the section title); AI-use disclosure is present when the repo's stated policy requires disclosing it in PRs (silence, or a policy that only asks for human review/understanding without asking for a stated disclosure, passes automatically); and the PR's approach follows any explicit maintainer (OWNER/MEMBER/COLLABORATOR) direction present in the thread, or there is none to follow. Fails if a required template section is visibly empty or boilerplate, required disclosure is absent, or explicit maintainer direction in the thread is ignored without acknowledgment. | required |

## Verdict rule

Accept (ready to submit) if and only if every `required` check above
grades `pass`. Any `required` check graded `fail` holds the package.
This rubric has no `preferred` checks; the slot is reserved for future
ranking-only checks. `unclear` counts as `fail` for every check: a
claim this tool cannot verify from the package — the diff, the plan,
the test evidence, or the repo's stated asks — is not ready to submit.
