# Evidence guide: where evidence lives in a PR package

<!--
THIS IS THE PART YOU WRITE (third week running: the map stays in your
hands). Your tool uses this guide as its map: for every kind of
evidence a rubric check names, this file says WHERE to find it in a PR
package and WHAT GOOD LOOKS LIKE when you do.

The four families below are the harness's failure categories under
the names the eval README uses: plan fidelity = silent-drift, test
evidence = not-tested, diff quality = unreviewable, standards and
comms = standards-wall. A package that fails none of them is a
clear-accept. Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the plan-context block's scope pair and test
  plan, the candidate PR's diff, commits, description, or
  test-evidence section, the repo-facts block's template asks and
  stated policy). In live mode (where in your working copy and on
  GitHub: your plan.md and its deviation notes, your branch's diff,
  your draft title and description, your captured test output, the
  repo's PR template and CONTRIBUTING.md).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("every changed file falls inside the
  plan's stated boundary or a deviation note") over adjectives ("the
  diff is clean").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute, and this week that cuts three ways: your
procedure says WHEN to gather each family, this guide says WHERE, and
your SKILL.md says the tool reads both. Write the map you wish your
executor had.
-->

## Plan fidelity (harness category: silent-drift)

**Where it lives.** In an eval bundle: the "Plan context" block's
scope/boundary statement and Files line, compared against the
candidate PR's "Diff" section (every file it touches) and its
"Description" (any sentence claiming what the change does or does not
do, relative to the plan). In live mode: `plan.md`'s Scope/Files
section and its `## Deviations` heading (filled in or not), compared
against `git diff main...HEAD` and the title/description in
`pr_draft.md`.

**What good looks like.** Every file the diff touches falls inside the
plan's stated scope, or a deviation note in `plan.md` (or the
equivalent plan-context block in eval mode) names the extra or missing
item and why. Drift runs in two directions, and both count: the diff
doing *more* than the plan (an unplanned refactor, a new option, an
unrelated file) with no deviation note, and the diff doing *less* than
the plan promised (a piece of the planned fix silently missing) with
no deviation note. Separately, read every fidelity-shaped sentence in
the description ("implements the plan exactly," "no changes beyond
it," "X now handles Y") against the diff itself — a description can
be honest about the plan while still lying about the diff, or vice
versa, so check both pairings, not just one. A plan that already
scoped something out from the start (not a late deviation, just a
boundary the plan drew on day one) is not a shortfall when the PR
doesn't include it. A reasonable paraphrase of implementation detail
("one function touched" when a small helper was factored out of that
same function to implement the fix) is not drift; drift is a
difference big enough to change what a reviewer would think the PR
does — an extra file, an extra feature, a behavior the description
never admits to.

## Test evidence (harness category: not-tested)

**Where it lives.** In an eval bundle: the candidate PR's "Test
evidence" section, compared against the plan-context block's stated
test plan (every scenario it names) and the repo-facts block's stated
required checks. In live mode: `test_evidence.md`, compared against
`plan.md`'s Test plan section, and the repo's own required commands
(for Path Review: `make test-unit`, `make test-integration`, `make
lint`, `make typecheck`, per the PR template).

**What good looks like.** The plan's *primary* scenario — the one that
actually demonstrates the bug/fix — is re-run with specific, concrete
before/after facts: an exact printed error, an exact exit code, an
exact returned value, an exact count. The trigger conditions must match
what the plan specified exactly: evidence that exercises a different,
easier, or already-working code path is not evidence for the plan's
claim, even when it's real output. Secondary scenarios/controls and the
repo's own required checks don't need a full raw terminal paste each,
but they do need at least one concrete, checkable detail apiece — "312
tests passed," "no diff in the generated file," "exit code 0 and both
query parameters present" are all fine; "tests pass," "works now,"
"verified" with nothing else attached are not, because there's nothing
in them a reviewer could actually check or dispute. A before/after
written as inline comments (`-- before: ...`, `# after: ...`) still
passes when the annotated values themselves are specific and concrete;
it fails when the comment is vague narration standing in for a value.
The repo's own required checks appear with their actual output
too; an honestly reported failure (the check ran, it failed, here's
why) is still valid evidence — it's the absence of real output,
honest or not, that fails this check.

## Diff quality (harness category: unreviewable)

**Where it lives.** The unified diff itself, hunk by hunk, and the
commit message list (commit messages like "wip," "fix," "fmt +
cleanup," or "misc cleanups while debugging" are themselves a signal
worth reading, not just the code).

**What good looks like.** The diff contains exactly the planned
change and nothing else a reviewer has to mentally filter out. Watch
for: debug print/log statements left in (`console.log`, `println!`,
`eprintln!`, a stray `print`); commented-out code, whether an
abandoned first attempt or a line someone meant to delete; dead code
(an unused function, often marked `#[allow(dead_code)]` or similar, as
a tell that the author already knew it was unused); pure formatting or
re-indentation churn that touches lines the fix didn't need to touch;
import reordering or restructuring the fix doesn't require. Any one of
these fails the check even when the actual fix underneath is correct
and well-evidenced — a reviewer having to dig the real change out of
noise is the harm, independent of whether the real change is right.

## Standards and comms (harness category: standards-wall)

**Where it lives.** The repo-facts block's stated PR-template sections
and contribution/AI-use policy (or, live, the repo's actual
`.github/PULL_REQUEST_TEMPLATE.md` and `docs/CONTRIBUTING.md`), and the
thread highlights for any explicit maintainer (OWNER/MEMBER/
COLLABORATOR) direction — read against the PR description's actual
content and the PR's chosen approach.

**What good looks like.** Every section the repo's template asks for
is filled with real, specific content: a checklist item is ticked only
when true of this PR, a "Closes #" line names the real issue, a
changelog/whatsnew entry exists where the template requires one. AI-use
disclosure, when the repo's stated policy requires disclosing it in
PRs, is a plain, specific statement — not silence, and not folded
invisibly into an unrelated section. A policy that only asks for human
review/understanding, or that is silent on AI use entirely, does not
require a disclosure statement to pass. Separately, if the thread
carries an explicit maintainer diagnosis or instruction, the PR's
approach either follows it or says plainly why it's doing something
else — ignoring it silently fails here even if the fix itself is
sound. (Whether the description's *claims* match the diff's actual
content is plan fidelity, above; this family is about meeting the
repo's and the thread's stated asks, not about truthfulness per se.)
