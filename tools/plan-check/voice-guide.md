# Voice guide: how I talk upstream

<!--
THIS IS THE PART YOU WRITE (new this week). Live mode reads this file
before any comment of yours goes out the door; eval mode ignores it
entirely, because your voice is yours and carries no gold labels.

This is not etiquette. "Be polite and concise" is advice for everyone
and therefore rules for no one. Write rules YOU need, in your own
words, each one concrete enough that the skill can hold a draft
against it and say which rule it breaks.

Three sections. Fill all three.
-->

## Who I am in threads

I'm a backend/Python-leaning developer making my first real
open-source contributions, still new to navigating large, unfamiliar
codebases. I say what I've actually verified and no more; I don't
claim expertise or certainty I don't have, and I'm upfront when I used
an AI assistant to help investigate or write something up.

## Rules I write by

### Rule: promise the approach, not a delivery date

A plan comment commits to a diagnosis and an approach — that's real
and fine to state plainly. What I don't commit to is a guaranteed
landing date or a promise that the PR will be perfect on the first
try; plans meet reality, and that's what Deviations is for.

- Wrong: "I will fix it within 2 days guaranteed, please keep this
  reserved for me."
- Right: "My plan is to [approach], scoped to [the one cause]. I'll
  post the PR once the test plan passes and report back if anything
  changes along the way."

### Rule: state exactly what happened, not how confident I feel about it

Confidence words don't substitute for evidence. If I paste an artifact,
I let it speak; I don't stack adjectives ("100% confirmed,"
"guaranteed reproducible") on top of it.

- Wrong: "I performed a careful and thorough investigation and can
  confirm this is fully reproducible."
- Right: "Here's the exact command I ran and what it printed."

### Rule: disclose AI assistance when the repo asks for it

I check the repo's contribution policy before I post. If it asks for
disclosure of AI-assisted work, I say so plainly, in my own words, and
I say what I personally verified myself.

- Wrong: (posting a claim or repro comment with no mention of AI use,
  on a repo whose policy requires disclosing it)
- Right: "I used Claude Code to help set up and write up this
  reproduction; I ran every step myself and can explain each one."

### Rule: promise one bounded fix, not a redesign

When I post a plan, I commit to the smallest change that addresses the
diagnosed cause, and I name anything bigger I noticed as a separate,
deferred idea — never as part of what I'm about to build. "While I'm
in here" is where scope creep starts.

- Wrong: "While I'm in here, I'll also migrate the fetch layer, add a
  settings field for it, and fix the silent-failure UI too."
- Right: "This plan is scoped to the one cause above. I noticed the
  fetch layer could use a cleanup too, but that's a separate follow-up,
  not part of this change."

### Rule: never claim exclusivity, even on a shared issue

Course credit (and, in the wild, good etiquette) attaches to the work I
post, not to locking a classmate or another contributor out.

- Wrong: "Please assign this to me only, I don't want anyone else
  working on it."
- Right: "I'd like to take a look at this; happy to coordinate if
  anyone else is already on it."

### Rule: an honest "I could not reproduce it" is a real result

If I try and it doesn't trigger, I say so plainly, backed by what I
actually tried and what differed from the report's conditions. That is
a legitimate, useful thing to post, not a failure to hide.

- Wrong: quietly not posting anything, or padding a failed attempt with
  unrelated confidence about the underlying bug.
- Right: "I could not reproduce this under X conditions; here's exactly
  what I ran and what's different about my setup from the report's."

## Things I never post

- A promised fix, a delivery date, or a demand that an issue be
  reserved for me alone.
- A plan that bundles unrelated improvements, migrations, or
  refactors into "while I'm in here" instead of naming them as
  separate, deferred follow-ups.
- A certainty claim ("100%", "guaranteed", "definitely") with no pasted
  artifact behind it.
- "Same as above, can confirm" on a shared issue without my own,
  actually-run reproduction.
- An AI-assisted comment on a repo whose policy requires disclosure,
  without disclosing it.
