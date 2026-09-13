# Fix expenses occasionally disappearing after saving

## Problem

- Type: Bug.
- Project: proj-pocket.
- Promise: the same expense remains visible after adding and refreshing.
- Mobile report: expenses occasionally disappear.
- Reported case: a TWD 85 Food expense disappeared.
- Reported time: ”yesterday”; exact date unknown.
- Version: Pocket web/pocket-0.3.1.
- Successful control: desktop Chrome retains a TWD 100 Transport expense after adding and refreshing.
- Evidence: requests.md C03.

## Current gaps

- Exact device unknown.
- Browser version unknown.
- Complete failure steps are unknown.
- Failure rate unknown.
- Observation time unknown.
- Console logs at failure are missing.
- Network logs at failure are missing.
- The localStorage snapshot at failure is missing.
- Hypotheses to investigate
  - iOS storage limitations.
  - Date-filtering problem.
- No causal evidence currently supports these hypotheses.

## Outcomes and order

1. Deliver the diagnostic evidence from [investigation-issue.md](investigation-issue.md).
2. Determine the fix location from evidence.
3. Define regression cases.
4. Draft the fix issue.
5. Perform overall acceptance on the fixed version.

## Overall acceptance

- [ ] The identified original failure scenario retains the same expense after the fix.
  1. Restore the affected environment from the investigation results.
  2. Add TWD 85 for Food using the failure steps.
  3. Refresh.
  4. Check that stored and displayed values match.
  5. Save the tested version and results.
- [ ] The desktop Chrome TWD 100 Transport control still passes.
- [ ] Regression checks pass for affected paths involved in the root cause.
- [ ] Regression records identify the tested version.

This item restores the existing persistence promise; the investigation determines the fix.
