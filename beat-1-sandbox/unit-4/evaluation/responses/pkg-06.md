Reject: the diff adds unplanned settings and theme-plumbing changes without deviations. The description also denies those changes, and unrelated restructuring adds debris.

```json
{
  "item": "pkg-06",
  "checks": [
    {
      "name": "Diff matches the plan's scope, or deviations are noted",
      "grade": "fail",
      "evidence": "GlobalAppSettings.idl adds MenuFollowsWindowTheme and Initialize changes theme/chrome plumbing outside the bounded menu fix; the promised IslandWindow.h change is absent, with no deviations recorded."
    },
    {
      "name": "Description's fidelity claims match the diff",
      "grade": "fail",
      "evidence": "The claim 'No functional changes outside the system menu fix' omits the new settings-model property and changes to theme event and chrome-brush plumbing."
    },
    {
      "name": "Test evidence is decisive and complete",
      "grade": "pass",
      "evidence": "The accepted repro records a light menu under system dark + Terminal dark; branch evidence reports a dark menu under that trigger, a light menu after switching to light, and Terminal.Unit.Tests with 0 failures."
    },
    {
      "name": "Diff is free of debris",
      "grade": "fail",
      "evidence": "Initialize renames the theme revoker, event handler, frame brush, and brush factory; this unrelated restructuring is also identified by the 'Rationalize theme update member naming and event plumbing' commit."
    },
    {
      "name": "PR meets the repo's stated template, policy, and thread direction",
      "grade": "pass",
      "evidence": "All five requested template sections contain specific content; no AI-disclosure requirement is stated, and the diff follows the IslandWindow pointer without using the prohibited private SetPreferredAppMode API."
    }
  ],
  "verdict": "reject"
}
```