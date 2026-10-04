# Procedure: how this skill grades a plan package

<!--
THIS IS THE PART YOU WRITE, and it is a new kind of part. Weeks 1 and
2, SKILL.md carried a numbered workflow and you only wrote judgment
files. This week the workflow is gone from the frame: SKILL.md says
"execute procedure.md", and these are the operating steps you author.
The machinery is in your hands now.

Your operator swap is the design brief. When your executor stalled
because your rubric said WHAT to decide but not HOW to find the
evidence, that was a procedure gap. This file is where those gaps get
closed: a complete procedure lets someone who has never seen a plan
package before (a groupmate, or the skill itself) grade one exactly the
way you would.

Under each stage heading below, write the concrete steps for that
stage. The one-line note under each heading says what a complete
procedure must decide there. Write steps, not intentions: "read the
repro evidence before the plan, and note what behavior it pins down"
is a step; "understand the context" is a wish.
-->

## Read order

<!-- What gets read, in what order, before any check is graded, and
what to note down from each part while reading. A complete procedure
decides the order (issue first? repro evidence first?) and says why
the order matters for the checks that come later. -->

1. Read the **issue** section first: the title, body, and labels. Note
   the stated bug/symptom in one sentence, in your own words, before
   reading anything else. This is the target every later check reads
   against.
2. Read **thread highlights** next, in order. Note, verbatim if
   possible, any comment from an OWNER/MEMBER/COLLABORATOR that states
   a cause, names a file or function, or includes a posted patch or
   test artifact. If none exists, note that explicitly ("no explicit
   maintainer direction in thread") rather than leaving it blank — a
   blank note and a checked absence must not look the same later.
3. Read the **repo-facts** block. Note the contribution policy's exact
   stance on AI-use disclosure (requires it / conditional, no
   disclosure ask / silent) in one line, quoting the operative phrase.
4. Read the **repro-evidence** block in full, step by step, in the
   order given. For every step, note what it establishes; for every
   step labeled "Control" (or that clearly varies one condition from
   the failing run), note exactly what varied and what the result
   was. This list is the yardstick for the Diagnosis-and-grounding
   check — build it before you have seen the candidate plan's stated
   cause, so the plan cannot anchor your reading of the evidence.
5. Read the **candidate plan** in full: diagnosis, scope/proposed
   changes, files, approach, test plan, risks — in that order, noting
   which section is the "built now" list and which (if any) is the
   "deferred / not in scope" list.
6. Read the **candidate plan comment** last, and read it the way a
   stranger on the GitHub thread would: on its own, without the extra
   detail `plan.md` carries. If the comment and the plan disagree on
   anything checked below, the comment is what a maintainer sees, so
   note the comment's version as the one that counts for Comms checks;
   the plan's version counts for every other check.

## Evidence gathering

<!-- For each evidence family your rubric's checks name, the concrete
gathering move: which part of the package (or, live, which page or
thread location per your evidence guide) to pull the fact from, and
what to record. A complete procedure leaves no check whose evidence an
executor would have to hunt for. -->

For each check below, pull evidence using the notes already taken in
Read order; do not re-read the whole package per check.

- **Diagnosis is grounded**: take the plan's stated cause (step 5's
  note) and the control-run list (step 4's note). For each control,
  ask: does the stated cause predict this exact result? Record every
  control that the cause fails to predict, with the control's own
  wording, as the evidence for a fail.
- **Scope is one bounded change**: from step 5's two buckets (built
  now / deferred), count the "built now" items. Record the full list;
  more than one distinct change in that list (beyond tests/regression
  coverage for the one change) is the evidence for a fail.
- **A stranger could start executing it**: from the plan's
  files/approach, record whether a specific file or location is named
  AND whether exactly one approach is committed to (not a menu of
  options, not "whichever is easier"). Both must be true to pass;
  record whichever is missing as the evidence for a fail.
- **Test plan is decisive**: from the plan's test plan section, record
  the exact expected result stated. Check it against the repro
  evidence's own artifacts/measurements (step 4's note): a passing test
  plan's expected result must be something you could confirm true or
  false by reading output alone, with no judgment call.
- **Honesty**: record every stated risk/unknown in the plan's closing
  section. Cross-check each flagged item against the Diagnosis check's
  finding: an item the plan calls settled that the diagnosis check
  itself could not fully confirm is the evidence for a fail. Separately
  check whether the plan's scope decision (e.g. a platform gate) comes
  with its own acknowledgment; a scope decision stated with zero
  caveats where the decision is itself a judgment call is also evidence
  for a fail.
- **Engages maintainer direction**: take step 2's note. If it recorded
  explicit direction, compare it against the plan comment's stated
  approach (step 6's note): does the approach follow it, or state a
  specific reason for doing otherwise? If step 2 recorded no explicit
  direction, this check passes automatically — record that as the
  evidence.
- **AI-use disclosure**: take step 3's note. If it recorded a
  disclosure requirement, scan the plan comment (step 6) and the plan
  (step 5) for an explicit AI-use disclosure statement; its presence or
  absence is the evidence. If step 3 recorded no requirement, this
  check passes automatically — record that as the evidence.

## Check execution

<!-- How one check runs against gathered evidence: in what order the
checks execute, what an executor does when evidence for a check is
genuinely absent, and when a check may be graded without re-reading
the whole package. A complete procedure makes two executors grade the
same package the same way. -->

1. Execute the seven checks in the order listed in `rubric.md`'s table
   (Diagnosis → Scope → Executability → Test plan → Honesty → Thread
   direction → AI disclosure). Grade each independently: a fail on an
   earlier check does not change how a later check is graded, and a
   later check's finding never retroactively changes an earlier one.
2. Apply each check's pass condition literally against the evidence
   gathered in the previous stage. Do not re-read the raw package text
   for a check whose evidence was already recorded there; use the note.
3. If a check's named evidence is genuinely absent from the package
   (for example, a package with no repro-evidence block at all, or a
   plan with no stated test plan section whatsoever) grade that check
   `unclear`, and say what is missing in the evidence field. Do not
   infer a default and do not treat silence as a pass unless the
   check's own pass condition says silence passes (the two
   comms-family checks both say this explicitly; no other check does).
4. Record, for every check, one line of evidence: a direct quote or a
   specific named fact (the control run's result, the exact deferred
   item, the maintainer's exact words, the policy's exact phrase) —
   never a restatement of the check's name or "looks fine."
5. Grade all seven checks before moving to verdict assembly, even once
   a reject is clear; the output must report every check's grade, not
   stop early.

## Verdict assembly

<!-- How the per-check grades become the final accept or reject:
apply your rubric's verdict rule, state how unclear grades enter it,
and say what gets quoted in the output for the deciding check. A
complete procedure produces the same verdict from the same grades,
every time. -->

1. Apply `rubric.md`'s verdict rule directly: `accept` if and only if
   all seven required checks graded `pass`; otherwise `reject`.
2. Treat every `unclear` grade as a `fail` for the purpose of this
   rule, per the rubric's stated default — there is no required check
   this rubric marks otherwise.
3. In the JSON output, every failing or unclear required check appears
   in the `checks` array with its recorded one-line evidence; do not
   collapse multiple failures into a single summary line.
4. In the short readable summary before the JSON block, name the
   single most decisive failing check first (the one whose evidence
   most directly contradicts the plan, e.g. a control run the
   diagnosis cannot explain, or a maintainer direction the comment
   ignores) so a re-reader knows where to look first, even when
   several checks failed.
5. On a `reject`, do not soften the verdict because other checks
   passed strongly; one required fail holds the package regardless of
   how good the rest of the plan is.
