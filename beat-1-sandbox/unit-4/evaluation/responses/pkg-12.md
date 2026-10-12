Reject: the diff includes unplanned changes without deviation notes. The description also claims a missing CHANGELOG entry, the control evidence lacks specifics, and debugging debris remains.

```json
{
  "item": "pkg-12",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "fail",
      "evidence": "The plan bounds the change to look-back allocation in Controller::print_file_ranges and one integration test; the import's added ring-buffer TODO and unused _unused_buffer_probe are unplanned changes with no deviation note."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "fail",
      "evidence": "The description claims 'regression test and CHANGELOG entry included,' but the diff contains no CHANGELOG entry."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "fail",
      "evidence": "The primary repro shows l1 and l2 with exit 0, and cargo test is reported passing, but the planned :-4 control is only called 'unchanged' without a specific returned value or concrete comparison."
    },
    {
      "name": "Diff is free of debris",
      "grade": "fail",
      "evidence": "src/controller.rs retains a commented-out eprintln!, a commented-out first allocation attempt, and the unused _unused_buffer_probe function."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "fail",
      "evidence": "The contribution guide requires tests and a CHANGELOG.md entry; the regression test exists, but the required changelog entry is absent from the diff."
    }
  ],
  "verdict": "reject"
}
```