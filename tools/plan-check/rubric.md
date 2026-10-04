# Rubric: is this plan ready to post and build from?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here (via your procedure.md). It ships empty on
purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the plan's scope statement, the test plan read against
     the repro evidence's steps, the plan comment read against the
     thread highlights, the repo-facts block) or a location from your
     references/evidence-guide.md. "The plan" is not a source; "the
     plan's stated cause read against what the repro evidence shows"
     is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (is
     this one bounded change? could a stranger start executing it?),
     never the write-up's shape (how many sections it has, how long it
     is, whether it uses headings). Structure-shaped checks are what
     make graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad plans posted. The lecture named the
failure families: the diagnosis ignores or contradicts the reproduced
evidence, the change is unbounded (scope creep), the plan targets the
symptom while the evidence points at the cause, a stranger could not
start executing it, the test plan proves nothing observable, the
unknowns are dressed up as certainty, and the comment ignores what the
thread or the repo's stated conventions ask. A rubric that ignores a
family will fail eval packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Diagnosis is grounded in the repro evidence | The plan's stated cause, read against every control/isolation run in the repro-evidence block (not just the main failing run). | Passes if the stated cause is consistent with and explains every control run's result, including by sound inference from the stated mechanism (e.g. "a cache clear forces one pass through the already-established-clean fresh-attach path, so one clean attempt before the reattach-only bug resumes" is applying the diagnosis, not inventing a new one). Fails only if a control run's actual observed result contradicts what the stated cause would predict, or a control isolates a different variable than the one the plan blames. A secondary control explained by straightforward extension of the main diagnosis is not "a new untested theory"; only fail/mark unclear when the *central* cause itself has no control or isolation step addressing it at all. | required |
| Scope is one bounded change | The plan's "Proposed changes"/"Change" section: what is committed to being built now, versus what is named as deferred or not-in-scope. | Passes if the committed work is one change addressing the diagnosed cause, and anything beyond that minimal fix (an alternative approach, a related improvement, a refactor, a new feature) is explicitly placed under a stated deferral/not-in-scope line rather than built now. Fails if the "Proposed changes" list itself commits to building multiple unrelated improvements, migrations, redesigns, or new features alongside the fix — including ones framed as "while in the area," "to do this properly," or "since we're already touching X." | required |
| A stranger could start executing it | The plan's stated files/locations and its approach/method of attack. | Passes if the plan names a concrete file, module, or location and commits to a single decided approach/strategy, such that someone could open that location and begin applying the approach without asking the author anything. A single decided approach at a named location still passes when the exact function name is left to be pinned down by tracing/debugging the author has already shown works (that is routine implementation detail, not an open decision). Fails only when the approach/strategy itself is undecided — a genuine choice between substantively different methods left open ("upstream or vendored, whichever is easier," "investigate and see what turns up," "whichever shows up hot in profiling") — or when no location/area is named at all. | required |
| Test plan is decisive | The plan's "Test plan" section, read against the repro evidence's own steps and artifacts. | Passes if the test plan names a specific, observable before/after outcome — an exact command or step and an exact expected result (output, exit code, measurement), ideally re-running the repro evidence's own steps. Fails if the expected outcome is a subjective feeling or adjective with no observable condition ("should feel fast," "should work better," "nothing else should feel broken") or if it names no concrete step at all. | required |
| Risk and unknowns are stated honestly | The plan's stated risks/open questions/unknowns, read against what the diagnosis check actually supports. | Passes if genuine unknowns (an untested assumption, an undecided trade-off, a deferred question) are flagged as open rather than asserted as settled, and the plan does not claim a certainty its own evidence doesn't support. Fails if the plan presents an untested assumption as a proven fact, or omits a risk that the plan's own approach obviously carries (e.g. a change gated to one platform with no acknowledgment that the gating itself is a judgment call). | required |
| Plan comment engages explicit maintainer direction | The plan comment's approach, read against any explicit maintainer (OWNER/MEMBER/COLLABORATOR) guidance in the thread highlights — a stated cause, a named file/function, a posted patch or test artifact. | Passes if, when the thread contains explicit maintainer direction about the cause or fix location, the plan comment's approach follows that direction, or states a specific reason it is doing something else instead. Also passes when the thread contains no such explicit direction (nothing to engage). Fails if explicit maintainer direction exists and the plan comment's approach ignores or contradicts it without any acknowledgment. | required |
| AI-use disclosure matches the repo's policy | The repo-facts "contribution policy" line, read against the plan comment (and the plan, as backup). | If the stated policy does not require disclosing AI assistance for comments (silence, a policy that only asks for human understanding/testing without asking for a stated disclosure, or a policy that scopes its disclosure ask to pull requests specifically) — passes automatically. If the policy requires disclosing AI assistance in comments, passes only if the plan comment (or the plan) contains an explicit statement disclosing AI use; fails if no such statement appears anywhere in the package. | required |

## Verdict rule

Accept (ready) if and only if every `required` check above grades
`pass`. Any `required` check graded `fail` holds the package.
`preferred` checks never change the verdict (this rubric currently has
none, but the slot exists for future ranking-only checks). `unclear`
counts as `fail` for every check: a plan whose grounding, scope,
executability, test plan, honesty, or conventions cannot actually be
verified from the package is not a plan that is ready to post and
build from.
