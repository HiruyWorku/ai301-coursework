# Procedure: how this tool grades a PR package

<!--
THIS IS THE PART YOU WRITE (second week running for the procedure).
Week 3 you wrote these steps for a plan package; this week the graded
object is a PR package, and the read that matters most is a
side-by-side: the diff against the plan, the evidence against the test
plan, the description against both. Your week-3 procedure is the
pattern; do not paste it unchanged, because its read order was built
for a different object.

Your rotation is the design brief again, and this week friction routes
three ways: a stall on WHAT to decide is a rubric gap, a stall on
WHERE to look is a procedure gap (this file), and a stall on what the
tool even reads or outputs is a frame gap (your SKILL.md). A complete
procedure lets someone who has never seen a PR package before grade
one exactly the way you would.

Under each stage heading below, write the concrete steps for that
stage. The one-line note under each heading says what a complete
procedure must decide there. Write steps, not intentions: "read the
plan's scope pair before opening the diff, and list the files the plan
names" is a step; "understand the change" is a wish.
-->

## Read order

<!-- What gets read, in what order, before any check is graded, and
what to note down from each part while reading. A complete procedure
decides where the plan sits in the order (before the diff? before the
description?) and says why the order matters for the side-by-side
checks that come later. -->

1. Read the **issue** first (its body, labels, and thread highlights).
   Note the bug/ask in one sentence, and note any explicit
   OWNER/MEMBER/COLLABORATOR direction verbatim — a stated cause, a
   named file, a posted patch — or note explicitly that none exists.
2. Read the **repo-facts block** next. Note the PR template's required
   sections exactly as listed, and the contribution/AI-use policy's
   exact wording on disclosure (required / conditional-no-disclosure-
   ask / silent).
3. Read the **plan context** in full: the plan's stated scope/boundary,
   its Files line, and its test plan (every named scenario, in order).
   Build this list *before* looking at the diff or description, so the
   diff cannot anchor your read of what was promised. Also note whether
   a `## Deviations` section exists and what it says.
4. Read the candidate **PR's diff**, file by file, in the order the
   diff presents them. For each file, note: is it in the scope list
   from step 3? Does the hunk contain only the planned change, or does
   it carry debris (debug statements, commented-out code, dead code,
   formatting churn, unrelated restructuring)? Build this as a table in
   your head (or scratch notes): file → in-scope? → debris found?
5. Read the candidate **PR's description** (title included) as a
   stranger on GitHub would — on its own, without the extra detail
   `plan.md` carries. Extract every fidelity-shaped claim (what the
   change does, does not do, or now handles) as a list of discrete
   sentences to check individually.
6. Read the **test evidence** last, matching it one-for-one against the
   test-plan list from step 3: for each named scenario, is there a
   corresponding before/after with real output? Separately note whether
   each repo-required check (from step 2, or named in the plan) appears
   with real output.

## Evidence gathering

<!-- For each evidence family your rubric's checks name, the concrete
gathering move: which part of the package (or, live, which file, diff,
or page per your evidence guide) to pull the fact from, and what to
record. The load-bearing gathers this week are pairings: diff files
against plan scope, claimed evidence against the plan's test plan and
the repo's checks, description claims against diff contents. A
complete procedure leaves no check whose evidence an executor would
have to hunt for. -->

- **Diff matches plan scope**: use step 4's per-file table against step
  3's scope list. Record every file NOT in scope, and every scope item
  from step 3 NOT present in the diff. For each such mismatch, check
  step 3's deviation-note record: does it name this exact item? Record
  the match/non-match per mismatched item.
- **Description matches diff**: take step 5's list of discrete claims.
  For each, check it directly against step 4's file-by-file notes and
  the diff's actual lines. Record, per claim, whether the diff supports
  it, contradicts it, or doesn't address it at all.
- **Test evidence decisive**: take step 6's scenario-by-scenario
  comparison. For each test-plan scenario, record: present with real
  output / present but narrated only / present but wrong trigger
  condition / absent entirely. Do the same for each repo-required
  check from step 2.
- **Diff free of debris**: take step 4's debris notes directly; no
  re-reading needed. Record each debris instance with its file and
  line context.
- **Standards and comms**: take step 2's template/policy notes and step
  1's maintainer-direction note. Check each required template section
  against step 5's actual description content (present with real
  content / present but boilerplate / missing). Check disclosure
  presence directly against step 5. Check the PR's chosen approach
  (from the diff and description together) against step 1's
  maintainer-direction note.

## Check execution

<!-- How one check runs against gathered evidence: in what order the
checks execute, what an executor does when evidence for a check is
genuinely absent, and when a check may be graded without re-reading
the whole package. A complete procedure makes two executors grade the
same package the same way. -->

1. Execute the five checks in the order `rubric.md` lists them (Diff
   matches plan scope → Description matches diff → Test evidence
   decisive → Diff free of debris → Standards and comms). Grade each
   independently: an earlier check's fail does not change how a later
   check is graded, and vice versa.
2. Apply each check's pass condition literally against the evidence
   recorded in the previous stage. Do not re-read the raw diff or
   description text for a check whose evidence was already recorded
   there; use the notes.
3. If a check's named evidence is genuinely absent (a package with no
   stated test plan at all, or a PR with no description whatsoever),
   grade that check `unclear` and say what's missing. Do not infer a
   default and do not treat silence as a pass unless the check's own
   pass condition explicitly says silence passes (only the disclosure
   half of "Standards and comms" says this; no other check does).
4. Record one line of evidence per check: a direct quote or a specific
   named fact (the exact file not in scope, the exact claim
   contradicted, the exact debris line, the exact missing section) —
   never a restatement of the check's name or "looks fine."
5. Grade all five checks before moving to verdict assembly, even once a
   reject is obvious; the output must report every check's grade.

## Verdict assembly

<!-- How the per-check grades become the final accept or reject:
apply your rubric's verdict rule, state how unclear grades enter it,
and say what gets quoted in the output for the deciding check: the
check whose failure the verdict turned on. When more than one check
failed, your procedure picks which one gets quoted (first failing
required check in rubric order is a fine rule); nothing picks it for
you, so write the rule down. A complete procedure produces the same
verdict from the same grades, every time. -->

1. Apply `rubric.md`'s verdict rule directly: `accept` if and only if
   all five required checks graded `pass`; otherwise `reject`.
2. Treat every `unclear` grade as a `fail` for this purpose, per the
   rubric's stated default.
3. In the JSON output, every failing or unclear check appears in the
   `checks` array with its recorded one-line evidence; never collapse
   multiple failures into one line.
4. When more than one check failed, the short readable summary before
   the JSON block leads with the **first failing required check in
   rubric order** (Diff matches plan scope, then Description matches
   diff, then Test evidence decisive, then Diff free of debris, then
   Standards and comms) as the headline reason, then lists the rest —
   this is the fixed tie-break rule, so the same package always leads
   with the same check.
5. On a `reject`, do not soften the verdict because other checks passed
   strongly; one required fail holds the package regardless of how good
   the rest of it is.
