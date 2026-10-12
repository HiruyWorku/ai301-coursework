Reject: the capacity check sits before the existing buffer reservation, rather than at the bulk-copy paths promised by the plan. The description overstates that change. Pre-commit evidence and required template content are also missing.

```json
{
  "item": "pkg-01",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "fail",
      "evidence": "The plan promises capacity checks before bulk copies; the diff adds a check before the existing make_stream_space call at tokenize_bytes entry, with no bulk-copy changes or deviation note."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "fail",
      "evidence": "The description claims a capacity check at the bulk-copy path after padding consumes the reservation; the added check precedes the existing buffer reservation and does not check subsequent copies."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "The exact repro reports 99999 before and 100000 after, a clean branch ASAN run, and 2841 parser tests passed, but the required pre-commit checks have no reported result."
    },
    {
      "name": "Diff is free of debris",
      "grade": "pass",
      "evidence": "The two-file diff contains capacity-check logic, explanatory comments, and a regression test; no debug statements, commented-out code, unused declarations, or unrelated formatting changes appear."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "fail",
      "evidence": "The required checklist and Closes #66657 line are absent, pre-commit completion is unreported, and the diff lacks the required whatsnew entry; no AI disclosure policy or explicit maintainer direction applies."
    }
  ],
  "verdict": "reject"
}
```