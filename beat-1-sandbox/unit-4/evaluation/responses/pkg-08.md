Reject: the tracked-change control says it “creates the stash” but gives no concrete stash entry, count, or state comparison. The primary repro is specific; the control falls short of the rubric’s evidence requirement.

```json
{
  "item": "pkg-08",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "pass",
      "evidence": "The diff changes only the files controller, English translations, and one integration test, implementing the planned guard and toast without changing stash semantics."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "pass",
      "evidence": "The AnyTrackedChanges guard returns CannotStashUntrackedOnly before Prompt; the translated message identifies stash-include-untracked and its default 'S' binding."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "The primary repro reports the exact toast, no prompt, and untracked.txt still listed, but the tracked-change control merely says it 'creates the stash' without a specific entry, count, or state comparison."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The hunks contain the stash guard, explanatory comments, translation, and integration test; no debug statements, abandoned code, dead code, or unrelated churn appear."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "PR Description and Requirements contain specific content addressing every template ask; the repo has no stated AI policy, and the thread contains no maintainer direction."
    }
  ],
  "verdict": "reject"
}
```