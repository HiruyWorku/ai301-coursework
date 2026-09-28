# Rubric: is this reproduction package ready to post?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here. It ships empty on purpose: the judgment is your
work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the claim comment, the repro report's environment
     record, the artifacts read against the issue's description, the
     repo-facts block) or a location from your
     references/evidence-guide.md. "The report" is not a source; "the
     output excerpt read against the error the issue describes" is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (does
     the artifact show the issue's behavior?), never the write-up's
     shape (how many steps it has, how long it is, whether it uses a
     template's headings). Structure-shaped checks are what make
     graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad packages posted. The lecture named the
proof families: the environment is recorded, the steps are complete
and followable, the behavior shown matches the issue (not an adjacent
one), the outcome is stated honestly (an evidenced cannot-reproduce is
a pass, a confident wrong-target is not), and the words respect the
repo's conventions. A rubric that ignores a family will fail eval
packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Claim promises investigation, not delivery | The candidate claim comment's own language about what happens next. | Passes if the claim states an intent to investigate and reports back, with no guaranteed fix, no committed delivery date or duration, and no demand that the issue be reserved or exclusively assigned to the author. Fails on any of those three: a promised fix, a named timeframe ("within 2 days", "by Friday"), or a reservation demand. | required |
| AI-use disclosure matches the repo's policy | The repo-facts "contribution policy" line, read against the claim comment and the repro report. | If the stated policy does not require disclosing AI assistance for issue/claim comments (silence, a policy that only asks for human understanding/testing without asking for a stated disclosure, or a policy that limits its disclosure ask to pull requests specifically) — passes automatically. If the policy does require disclosing AI assistance in comments, passes only if the claim comment or the repro report contains an explicit statement disclosing AI use; fails if no such statement appears anywhere in the package. | required |
| Environment recorded | The repro report's stated tool/library version and OS/platform. | Passes if the report names the specific version of the tool/library under test and the OS/platform used to attempt the reproduction. Fails if either is absent, or if the issue's bug is itself platform/build-specific (e.g. driver, build profile, Windows build number) and the report omits that specific detail. | required |
| Steps are followable by a stranger | The repro report's stated commands, flags, and input content. | Passes if every step needed to attempt the reproduction is specified precisely enough that a stranger with only the issue and the report (no access to the author's machine or private files) could reconstruct and run the identical steps without guessing any choice that affects whether the bug triggers. A literal pasted block is one way to satisfy this, but a precise description is equally sufficient when it leaves nothing ambiguous about the parts that matter to the trigger (e.g. "a valid dependencies list plus one added `category:` key" is fully determined when the issue's bug is about the extra key, not about which packages are listed). Fails if any essential step depends on unshareable material (a private repo, an unshared config), omits a flag/parameter the issue's own repro depends on, or describes an input vaguely enough that a stranger would have to guess something that could change the outcome. | required |
| Version or build delta is acknowledged | The repro report's stated version/build, compared against whatever version(s) the issue's own reporter explicitly states or confirms the bug on (a "Version:" field, an environment block, or explicit "confirmed on X" wording in the issue body itself — not a version number a different commenter merely speculates is related). | Passes if the report's version matches what the issue's reporter states, if the issue names no specific version at all (nothing to deviate from), or if the report's version differs from the reporter's and the report explicitly names that difference. Fails only if the issue's reporter explicitly states an affected version, the report silently uses a different one, and the report never mentions the difference. | required |
| Evidence attached | Literal pasted terminal output, log excerpt, screenshot, or exit code in the repro report, from actually running the steps. | Passes if at least one such literal artifact is present. Fails if the report only describes what supposedly happened, with no pasted artifact from an actual run. | required |
| Artifact matches the issue's specific behavior | The artifact from "Evidence attached," read against the issue's own stated symptom, trigger condition, and failure class (error type, exit code, crash vs. no crash). | Passes if the artifact demonstrates the SAME specific behavior the issue describes — matching trigger syntax where the issue specifies exact syntax, and matching failure class (a described crash is shown as a crash, not a milder validation error; a described error is the same error, not a different one produced by a modified input) — or if the report honestly states it could NOT reproduce, backed by a real, described attempt and a account of what differed. Fails if the artifact shows a different, milder, or absent symptom than the one the issue describes, even when the report's own narration claims a match. | required |

## Verdict rule

Accept (ready) if and only if every `required` check above grades
`pass`. Any `required` check graded `fail` holds the package.
`preferred` checks never change the verdict (this rubric currently has
none, but the slot exists for future ranking-only checks). `unclear`
counts as `fail` for every check: proof that cannot be verified is
proof that is not ready to post.
