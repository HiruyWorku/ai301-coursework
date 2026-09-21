# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Not archived | The repo line's `archived:` flag (repo-facts block; on github.com, the "This repository has been archived" banner). | `archived: no`. An archived repo is read-only: no PR of yours can ever merge. | required |
| Recent repo activity | The "last push to any branch" date in the repo-facts block (on github.com: the date on the newest commit on the front page). | Last push is within 180 days of the bundle's capture date (live mode: within 180 days of today). A repo that hasn't moved in 6 months is not a place a first PR gets reviewed. | required |
| Bounded scope | The issue title, body, and labels, plus how the thread discusses the work (repo-facts gives none of this; it is all in the Issue/Comments sections). | Fails if the issue is any of: (a) an explicit umbrella/tracking issue whose own text invites multiple *different contributors* to each pick a *different* sub-item as their *own separate* PR ("megaissue", "PRs welcome both big and small... anywhere in the codebase", a checklist where each box is claimed by a different person); (b) a feature request or design question with no maintainer-endorsed concrete spec, especially one with named open design decisions still unresolved ("out of scope for v1", "TBD") or years of back-and-forth with no maintainer sign-off on a final approach; (c) a pure usage/support question ("how do I get this to work?") with no requested code change. Passes even when the single requested change has several concrete steps, edits several files, updates several docs pages, or (for a bug) names several candidate causes and several possible fix approaches for that one symptom — none of that is an umbrella, because it is still one contributor delivering one fix or one feature in one PR. Only fail on a numbered/checklist body when the items are separable pieces of work the issue itself frames as being claimed and shipped independently (different sub-tasks for different contributors/PRs), not when the numbers are just a diagnosis or a menu of implementation options for a single change. Its shape must already be settled (by the issue body itself, or by a maintainer in the thread) rather than still being designed. A terse body, a bug report without repro steps, or a maintainer-filed issue can still pass: judge whether the work is one settled, single-PR-sized change, not the polish of the writeup or the number of files/options it lists. | required |
| Unclaimed | The `assignees:` and `linked PRs:` lines under "this issue" in the repo-facts block, plus any PRs mentioned in the comment thread (references/evidence-guide.md, Family 4). | Fails if any of: (a) `assignees` lists anyone; (b) any linked or thread-mentioned PR is currently `open` (a `closed` or `merged` linked PR is a past, abandoned, or already-landed attempt and does not fail this check); (c) the most recent claim comment ("I'll take this" / "working on this") in the thread is less than 180 days old and no bot or maintainer comment marks it abandoned or unassigned. An old claim (180+ days, no linked open PR, no recent follow-up) is stale and does not fail this check. | required |
| Contribution policy allows AI-assisted work | The "contribution policy" line under Repo facts (references/evidence-guide.md, the fifth surface; on github.com: `CONTRIBUTING.md` or `.github/`). | Fails only on an outright ban on AI-generated contributions ("we do not accept AI-generated code"). Conditions (disclosure, understanding, testing, human review) are terms to follow, not bans, and pass. A policy banning only "fully AI-generated" work while allowing assistive/reviewed AI use passes. No stated policy passes (silence passes). | required |
| Maintainer responsiveness | The "maintainer first-response sample" list in the repo-facts block (on github.com: reply times on a handful of recently updated issues, badge-holders only). | Passes if at least one sampled issue shows an owner/member/collaborator first response within 30 days. This never blocks a verdict; it only ranks accepted issues (a repo with fast maintainer replies is a better bet than one with none in the sample, even if both are otherwise alive). | preferred |
| Well-specified fix | The issue body: does it name the exact files/behavior to change, or does a maintainer state the cause? | Passes if the body or thread names concrete files, functions, or a diagnosed cause, rather than only describing a symptom. Ranks accepted issues only; a symptom-only bug report is still acceptable if scope and liveness pass. | preferred |

## Verdict rule

Accept if and only if every `required` check grades `pass`. Any `required`
check that grades `fail` rejects the issue. `preferred` checks never
change the verdict; they only order the accepted issues (more `pass`
preferred checks ranks higher).

`unclear` is treated as `fail` for every check, required or preferred: a
first issue whose liveness, scope, claim status, or policy status cannot
actually be verified from the evidence is not a first issue to take on
faith.
