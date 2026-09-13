# Fix expenses occasionally disappearing after saving

## Problem

- Type: Bug; Project: proj-pocket.
- Promise: the same expense remains visible after adding and refreshing.
- User report: occasionally on mobile; one TWD 85 Food expense disappeared ”yesterday” in the report; exact date unknown.
- Version: Pocket web/pocket-0.3.1.
- Successful control: desktop Chrome retains a TWD 100 Transport expense after adding and refreshing.
- Evidence: requests.md C03.

## Current gaps

- Device and browser versions unknown.
- Complete failure steps, rate, and observation time are unknown.
- Console, network, and localStorage snapshots at failure are missing.
- iOS storage limitations and date filtering are discussion hypotheses without causal evidence.

## Outcomes and order

1. First deliver reproduction and diagnostic evidence in investigation-issue.md.
2. Determine the fix location and regression cases from evidence, then draft the fix issue.
3. Perform this item’s overall acceptance on the fixed version.

## Overall acceptance

- [ ] The identified original failure scenario retains the same expense after the fix.
  1. Reproduce using the device, version, and steps from the investigation.
  2. Add TWD 85 for Food on the fixed version and refresh.
  3. Check that stored and displayed values match; record the tested version and results.
- [ ] The desktop Chrome TWD 100 Transport control still passes.
- [ ] Regression checks pass for affected paths involved in the root cause, with version evidence.

This item restores the existing persistence promise; the investigation determines the fix.
