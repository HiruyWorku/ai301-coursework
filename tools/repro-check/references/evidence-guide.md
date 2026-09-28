# Evidence guide: where proof lives in a reproduction package

<!--
THIS IS THE PART YOU WRITE (new this week: Unit 1 handed you this file
finished; the scaffolding fades). The skill uses this guide as its map:
for every kind of proof a rubric check names, this file says WHERE to
find it in a package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repo-facts block, the
  claim comment, the repro report and its parts). In live mode (where
  on GitHub or in the draft: the issue thread, the repo's docs, the
  student's draft comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the versions named match what the
  issue targets, or the difference is called out") over adjectives
  ("environment is thorough").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute; the rubric swap showed you what that feels
like. Write the map you wish your grader had.
-->

## Environment

**Where it lives.** In an eval bundle: the first line(s) of the
"Candidate repro report" section, usually starting "Environment:" —
tool/library version, install method, OS, and any other named
component (shell, browser, kernel, dependency versions). In live mode:
the equivalent line in the student's own draft repro report; the
issue's own stated environment (its "Version:"/"Operating system:"
lines, or its bug-report-template answers) is the target to compare
against, found in the issue body or the repo-facts block's "bug
reports" line (what the template asks for).

**What good looks like.** The tool/library version and OS/platform are
both named as plain facts, not adjectives ("thorough," "detailed"). If
the issue's own bug is platform- or build-specific (a driver flag, a
Windows build number, a debug-vs-release build, a browser), the report
names that specific detail too, not just a generic OS name. Silence on
any of these ("Windows 11" with a build-specific bug and no build
number; no version at all) is a miss, not a style choice.

## Steps

**Where it lives.** The "Steps"/"Reproduction"/"Preparation" +
"Execution" portion of the candidate repro report: the exact commands
run, exact flags, and exact contents of any input file created. In live
mode, also check whether any named file, config, or repo the steps
depend on is something a stranger could actually obtain (public vs.
private).

**What good looks like.** Every command needed to trigger the issue is
written out in full and copyable ("ran the command from the issue" is
not a step; the literal command is). Input content can be pasted
verbatim or precisely described, as long as the description leaves
nothing ambiguous about whatever actually matters to the trigger — a
described input is fine when any unconstrained detail (arbitrary
package names in an otherwise-specified file, say) couldn't change
whether the bug fires. A step is unfollowable if it silently depends on
something a stranger cannot get: a private repository, an unshared
internal config file, a machine-specific path with no equivalent given.
Cross-check against the issue's own repro steps: an omitted flag or
setting the issue's steps included (e.g. a `--driver` flag on a
driver-specific bug) breaks followability even if the rest reads
cleanly.

## Behavior shown

**Where it lives.** The literal pasted terminal output, log excerpt,
screenshot description, or stated exit code inside the candidate repro
report — read side-by-side with the issue's own stated actual behavior
(its own pasted output, its "Actual behavior:" text, or a maintainer's
comment pinning down the exact trigger, e.g. "it's not just X, Y is
also required").

**What good looks like.** The artifact shows the *same* failure class
the issue describes: if the issue reports a crash/panic, the artifact
shows a crash/panic (not a graceful validation error, not "the process
stayed alive"); if the issue names an exact input syntax as the
trigger, the artifact's command uses that exact syntax (a syntax
variant that produces a different, milder error is not the same bug,
however similar it looks at a glance). An artifact that merely shows
the tool starting up, or the environment being set up, without ever
displaying the specific claimed symptom, does not show the behavior —
it shows the setup for showing it. Compare the *exact* wording/class of
error or crash, not just "an error happened."

## Honesty

**Where it lives.** Compare the repro report's stated conclusion
("Expected"/"Actual", or an explicit result line) against what its own
artifact (see "Behavior shown" above) actually contains.

**What good looks like.** The conclusion never claims more than the
artifact shows. A report that says "I could not reproduce this" and
backs that with a real, described attempt and what differed from the
issue's conditions is honest and passing material — cannot-reproduce is
a legitimate, valuable outcome. A report that asserts a match, a root
cause, or a "guaranteed" reproduction without a supporting artifact (or
whose artifact contradicts the claim — e.g. "the terminal is verifiably
broken" pasted next to output showing the terminal still running) is
not honest, regardless of how confidently it is worded. Judge the gap
between claim and artifact, not the confidence level of the prose.

## Comms

**Where it lives.** The candidate claim comment, read against: (a) the
issue itself (does it name the actual issue and a real, specific next
step, or is it generic/boilerplate?), and (b) the repo-facts
"contribution policy" line (does the repo require anything about
AI-use disclosure, and if so, does the comment satisfy it?).

**What good looks like.** The claim names the specific issue and a
concrete, honest next action ("I want to check X against Y"), and
promises investigation only — never a fix, a delivery date, or an
exclusive claim on the issue. On AI-use disclosure specifically: read
the contribution-policy line's exact wording — a policy demanding
disclosure "in comments" or "in any form" is not satisfied by silence;
a policy that only asks for human review/understanding, or that scopes
its disclosure ask to pull requests, does not require a comment-level
disclosure statement at all.
