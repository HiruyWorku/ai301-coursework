# Evidence guide: where evidence lives in a plan package

<!--
THIS IS THE PART YOU WRITE (second week running: the judgment files
stay in your hands). The skill uses this guide as its map: for every
kind of evidence a rubric check names, this file says WHERE to find it
in a plan package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repro-evidence block,
  the candidate plan's scope statement or test plan, the plan comment,
  the repo-facts block). In live mode (where on GitHub or in the
  draft: the issue thread, the student's posted repro comment, the
  repo's docs, the draft plan and comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the stated cause cites behavior the
  repro evidence actually shows") over adjectives ("diagnosis is
  solid").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute, and this week that cuts twice: your
procedure.md tells the skill WHEN to gather each family, and this
guide tells it WHERE. Write the map you wish your executor had.
-->

## Diagnosis and grounding

**Where it lives.** In an eval bundle: the "Repro evidence" section's
numbered steps and, especially, its **control/isolation runs** (any
step labeled "Control" or that varies exactly one condition from the
failing run) — these are the yardstick, not the main failing run
alone. The plan's own "Diagnosis" (or equivalent opening) section
states the cause to check against them. In live mode: the student's
own posted Unit 2 repro comment (or the house repro pack) in place of
the bundle's repro-evidence block; the draft `plan.md`'s diagnosis
section in place of the candidate plan.

**What good looks like.** The stated cause explains *every* control
run's result, not just the headline failure: if a control shows the
same inputs succeeding once one condition changes, the stated cause
must predict that change in outcome. A diagnosis that would predict
the opposite of what a control shows (the "operator-swap" trap: a
confident cause that a close read of the control runs actually rules
out) fails, however polished the write-up. A diagnosis is also
ungrounded if it rests on a theory the repro evidence never tested at
all (nothing to confirm or rule it out) rather than one the evidence
actively contradicts — treat that as `unclear`, not a pass.

## Scope

**Where it lives.** The plan's "Scope," "Proposed changes," or
"Change" section: read it as two buckets — what is stated as being
built now, and what is named as deferred, "not in scope," or left for
a follow-up. In live mode, the same two buckets inside the draft
`plan.md`.

**What good looks like.** Exactly one committed change addresses the
diagnosed cause. A second (or third, fourth...) committed action item
in the same section — a migration, a new option, a UI addition, a
"let's fix the whole pipeline" reframing — is scope creep even when
every individual piece sounds reasonable on its own, and even when
introduced as "while already in the area" or "to do this properly."
The tell for a *legitimate* deferral is that the extra idea sits under
an explicit not-in-scope/deferred line with a stated reason, not inside
the list of things that will be built in this change.

## Executability

**Where it lives.** The plan's "Files," "Approach," or equivalent
section: the named files/functions/locations, and the stated method
(not menu of methods) for making the change.

**What good looks like.** A stranger could open the named file and
start on step one without asking the author anything. Fails this check
when the plan defers a real decision to build time instead of making
it now: "upstream or vendored, whichever is easier," "recover()
somewhere," "investigate X and see," a profiling step with no
committed follow-up action. Naming a file with no committed approach,
or an approach with no file, both fail; a plan can be short and still
pass as long as every decision that matters is actually made.

## Test plan

**Where it lives.** The plan's "Test plan" section, read against the
repro-evidence block's own steps, commands, and artifacts (its exact
output, exit codes, or measurements).

**What good looks like.** The test plan names a specific command or
step and a specific expected result — ideally the repro evidence's own
failing command, now expected to produce a named different, observable
output (ties back explicitly: "re-run step 2, expect exit 0" rather
than "re-test and confirm it works"). An adjective-only outcome
("should feel fast," "should work better," "nothing else should feel
broken") is not decisive even when the rest of the plan is excellent;
a stranger running the test plan must be able to say pass/fail from
the observable result alone, without the author's judgment.

## Honesty

**Where it lives.** The plan's "Risk," "Unknowns," or equivalent
closing section, read against what the Diagnosis-and-grounding check
above actually supports, and against the plan's own stated scope
decisions (e.g. a platform-gated fix, a deferred alternative).

**What good looks like.** A genuine unknown (an untested assumption, a
trade-off not yet measured, a question left for review) is named as
open, in its own words — this is a pass, not a weakness; the course's
clear-accept packages often include exactly this ("I have not yet
measured X; if Y, I will do Z instead, flagging the trade-off for
review"). It fails when the plan asserts something as a settled fact
that only the diagnosis check would actually need to support (claiming
certainty the evidence doesn't back), or silently omits an unknown its
own approach obviously carries (a platform-specific change with no
acknowledgment that the gating is itself a judgment call).

## Comms

**Where it lives.** The plan comment, read against two separate
things: (1) the thread highlights (or, live, the real issue thread)
for any explicit maintainer (OWNER/MEMBER/COLLABORATOR) direction — a
stated cause, a named file, a posted patch or test artifact, an
explicit ask ("please test this"); and (2) the repo-facts
"contribution policy" line (or, live, `CONTRIBUTING.md`/`AI_POLICY.md`)
for any AI-use disclosure requirement.

**What good looks like.** On maintainer direction: the plan comment's
approach either follows the direction already given, or says plainly
why it is doing something else — silently ignoring a maintainer who
already pinned the file and posted a patch, in favor of an unrelated
workaround, fails even when that workaround is itself well-written. On
disclosure: read the policy's exact wording — "must be disclosed, in
any form" is not satisfied by silence; a policy that only asks for
human review/understanding, or that scopes its disclosure ask to pull
requests, does not require a comment-level disclosure statement at
all. Every package (and every real comment a student posts) is treated
as AI-assisted work for this check.
