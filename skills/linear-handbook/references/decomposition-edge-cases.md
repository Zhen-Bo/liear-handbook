# Decomposition edge cases

The following three cases are tabletop exercises for fictional products.
Paths in the cases name planned artifacts.
Acceptance lists describe evidence to obtain during execution.
Quantity and time thresholds are assumptions for these cases.

- Method: [Single-session decomposition guide](issue-decomposition.md).
- Comparison: [Feature decomposition example](feature-decomposition.md).

Decompose work into outcomes that can be handed off.
Each sub-issue includes its own required verification.
If one session can deliver the whole outcome, combine it into one issue.
The number of sub-issues here is not a quota for other work.

## Case 1: Bug with an unknown root cause

### Parent: Restore the expired password-reset link message

Starting requirement: [Bug template](../assets/templates/bug.md#completed-example).
This variation only establishes that the loading screen persists; the actual API response still needs investigation.

- Actual behavior: opening a link issued 31 minutes ago keeps showing the loading screen.
- Promised behavior: links older than 30 minutes display “This link has expired. Please request a new one.”
- Scope: restore the existing expired-link message.
- Reproduction input: a test account with a controllable link issue time.

Integration acceptance:

- [ ] An expired link displays the specified message.
  1. Create a link issued 31 minutes ago in the integration environment.
  2. Open it in a browser that is not signed in.
  3. Confirm the loading screen disappears.
  4. Confirm “This link has expired. Please request a new one.” is displayed.
- [ ] A link issued 5 minutes ago can complete a password reset.
- [ ] The new password can be used to sign in.

### Sub-issue: Find the failure cause and determine the fix scope

Use the [Research template](../assets/templates/research.md#instructions) for the investigation.

- Inputs
  - The parent's failure scenario.
  - The affected version.
  - Request-tracing access in the test environment.
- Outputs
  - `investigation/expired-reset.md`: diagnostic conclusions.
  - `fixtures/expired-reset/`: reproducible data.
- Scope
  - Compare actual request paths for expired and valid links.
  - Trace why the screen never finishes loading.
  - Select the smallest fix boundary supported by evidence.
  - Reassess remaining evidence needs after two hours of investigation.
- Acceptance
  - [ ] A successor can reproduce the failure from the record.
  - [ ] Request records identify the affected version.
  - [ ] Experiments or code evidence support the diagnosis.
  - [ ] Evidence is sufficient to determine the fix scope.
  - [ ] The fix scope has regression scenarios with determinable results.

If the time limit is reached without a fix scope, preserve the evidence and hand off the investigation.
Listing possible causes alone does not satisfy this sub-issue's acceptance.
Create only this investigation sub-issue before diagnosis.

### Fix sub-issue created only after diagnosis

The following assumes the investigation proves that the API already returns `410 / TOKEN_EXPIRED`.
This branch of the exercise adopts a frontend error path that does not finish loading as its root cause.
If actual evidence differs, rewrite the subsequent work from the diagnosis.

Sub-issue title: Make the reset page display expired responses correctly.

- Inputs
  - Accepted diagnostic conclusions.
  - Reproduction data for the expired response.
- Outputs
  - Version entry point for the reset-page error-handling change.
  - `tests/expired-reset/`: regression checks.
- Scope
  - Finish loading after receiving an expired response.
  - Display the message specified by the parent.
- Acceptance
  - [ ] A simulated expired response displays the specified message.
  - [ ] The loading screen disappears after a simulated expired response.
  - [ ] A valid response still enters the password-setting flow.

### Sub-issue: Verify the real password-reset flow

- Inputs
  - A deployable fixed version.
  - The parent's test account.
- Outputs
  - `verification/expired-reset.md`: integration version and acceptance evidence.
- Scope
  - Verify the actual reset flow in the browser.
- Acceptance
  - [ ] All parent integration acceptance criteria pass.
  - [ ] Each result identifies the actual version and evidence.

### Dependencies and new requirements

- The fix waits for the diagnosis because evidence to support its boundary is missing.
- Real-flow verification waits for a deployable fix because simulated responses cannot establish end-to-end behavior.
- Do not start investigation and implementation simultaneously under different assumptions.
- A new request to resend email directly from the expired page adds a capability.
  - Create a separate Feature with email acceptance criteria.
  - The requirement decision-maker confirms whether it belongs in this delivery.
  - Retain the original message acceptance until adopted.
- If the diagnosis finds another path that also breaks the existing message, update the parent with that gap.
  - Split out a separately verifiable sub-issue if the repair exceeds one session.
  - Integration acceptance waits for that required fix.

## Case 2: Refactoring across modules

### Parent: Centralize order total calculation

Starting requirement: [Refactoring template](../assets/templates/refactor.md#completed-example-centralize-order-total-calculation).

- Current structure: the HTTP handler and background worker each have an amount formula.
- Target structure: both entry points call one domain implementation.
- External contract
  - Two items priced at 100 each total 200 without a discount.
  - A 10% discount produces a total of 180.
  - An invalid discount preserves the HTTP 400 response.
  - An invalid discount preserves the worker's existing failure record.

Integration acceptance:

- [ ] Both entry points call the single domain calculation implementation.
- [ ] Neither entry point contains a duplicate discount formula.
- [ ] Actual HTTP requests satisfy the external contract applicable to HTTP.
- [ ] Actual background jobs satisfy the external contract applicable to the worker.

### Sub-issue: Confirm the behavioral baseline and deliver the shared calculation core

- Inputs
  - Existing implementation versions of both entry points.
  - The parent's external contract.
- Outputs
  - `contracts/order-total.md`: input and result contract.
  - `src/domain/order-total.ts`: shared implementation.
  - `tests/order-total/`: behavioral baseline.
- Scope
  - Compare amount results from both entry points first.
  - Record how existing errors map to each entry point.
  - Extract the pure calculation responsibility.
- Acceptance
  - [ ] The shared core passes the 200 case.
  - [ ] The shared core passes the 180 case.
  - [ ] Invalid-discount results can preserve both entry points' original error contracts.
  - [ ] The HTTP successor can integrate using the contract.
  - [ ] The worker successor can integrate using the contract.

If comparison finds different existing amounts across the entry points, first confirm the contract to preserve.
Do not silently unify unresolved behavior under the name of refactoring.
If promised behavior needs correction, create a separate Bug and update required prerequisites.

### Sub-issue: Connect the HTTP entry point to the shared core

- Input: accepted shared core and contract.
- Output: version entry point for the HTTP integration change.
- Scope: replace amount calculation inside the HTTP entry point.
- Acceptance
  - [ ] An HTTP request without a discount returns a total of 200.
  - [ ] An HTTP request with a 10% discount returns a total of 180.
  - [ ] An invalid discount preserves the 400 response.
  - [ ] The HTTP entry point no longer contains the discount formula.

### Sub-issue: Connect the worker to the shared core

- Input: accepted shared core and contract.
- Output: version entry point for the worker integration change.
- Scope: replace amount calculation inside the worker.
- Acceptance
  - [ ] A background job without a discount produces 200.
  - [ ] A background job with a 10% discount produces 180.
  - [ ] An invalid discount preserves the existing failure record.
  - [ ] The worker no longer contains the discount formula.

### Sub-issue: Verify the integrated version of both entry points

- Inputs
  - HTTP integration version.
  - Worker integration version.
- Output: integration evidence in `verification/order-total.md`.
- Scope: check structure and external behavior on the same version.
- Acceptance
  - [ ] All parent integration acceptance criteria pass.
  - [ ] Evidence identifies the same core version used by both entry points.

### Dependencies and new requirements

- Both integration sub-issues wait for a usable core because their acceptance needs actual calculation results.
- Once the core is usable, HTTP and worker integration can proceed in parallel.
  - Each calls the same core contract.
  - Each verifies its own external entry point.
- Integration waits for both entry-point versions to verify that the single implementation is in use.
- Coordinate shared-file changes first; overlapping files alone do not establish an artifact dependency.
- Create a separate Feature for a new request to support tiered discounts.
  - First decide whether it belongs in this delivery.
  - Update the external contract after adoption.
  - Reassess acceptance for both integration sub-issues when the contract changes.

## Case 3: Data migration

### Parent: Switch ten test accounts' preferences to the new format

Starting requirement: [Migration template](../assets/templates/migration.md#completed-example-convert-test-account-preferences-to-the-new-format).

- Scope: the ten accounts listed in `migration/cohort.txt`.
- Old state: `preferences-v1.json`.
- Target state: `preferences-v2.json`.
- Mapping rules
  - Convert `theme=dark` to `appearance=dark`.
  - Convert `theme=light` to `appearance=light`.
  - Convert an unset `theme` to `appearance=system`.
  - Preserve original values in all other fields.
- Cutover: pause writes to this cohort during a maintenance window.
- Retirement: disable this cohort's v1 entry points.
- Backup retention: retain the v1 backup for seven days.

Integration acceptance:

- [ ] All ten accounts read preferences from v2.
- [ ] The account ID set is identical before and after migration.
- [ ] Every account satisfies the field mapping rules.
- [ ] The recovery rehearsal proves that new writes are not lost.
- [ ] There are zero parsing errors during a fifteen-minute observation period.
- [ ] This cohort's v1 entry points are disabled.
- [ ] After resuming v2 writes, a preference can be saved and read back.
- [ ] The v1 backup retention period is configured.

### Sub-issue: Confirm data conditions and rehearse conversion and recovery

- Inputs
  - A copy of this cohort's data.
  - The parent's field mapping rules.
  - A list of every write entry point for this cohort.
- Outputs
  - `scripts/migrate_preferences.py`: conversion tool.
  - `migration/runbook.md`: cutover and recovery operations.
  - `migration/rehearsal.md`: rehearsal results.
- Investigation prerequisites
  - Check whether actual field values fit the mapping rules.
  - Determine whether background jobs modify this cohort's data.
  - Confirm the pause mechanism prevents every write to the cohort.
  - Confirm accepted in-flight writes can be identified and drained.
- Scope
  - Complete conversion on an isolated copy.
  - Rehearse recovery within the rollback window.
  - Rehearse forward repair after v2 writes resume.
- Acceptance
  - [ ] Unknown field values have an explicit handling decision.
  - [ ] Every write entry point rejects new writes during maintenance.
  - [ ] Accepted in-flight writes finish before backup.
  - [ ] The account ID set is identical after converting the copy.
  - [ ] Every field in the copy satisfies the mapping rules.
  - [ ] The rollback rehearsal restores the same SHA-256 as the backup.
  - [ ] The forward-repair rehearsal preserves data written after writes resume.
    1. Write an identifiable new preference to the converted copy.
    2. Inject a recoverable read failure.
    3. Pause writes and drain accepted writes.
    4. Save the latest v2 copy.
    5. Follow the runbook to repair reads while preserving the latest data.
    6. Confirm the new preference accepted before the failure is still readable.
    7. Resume writes and confirm another preference can be saved.

Cutover remains unable to start while any required data condition is unresolved.
If investigation exceeds the session, preserve evidence using the [handoff workflow](issue-decomposition.md#handling-work-that-exceeds-a-session).

### Sub-issue: Execute the cohort cutover and verify the user flow

- Inputs
  - The conversion tool version that passed rehearsal.
  - The accepted runbook.
  - Cutover permission for the cohort's environment.
- Outputs
  - The cohort operating on v2.
  - `verification/preferences-cutover.md`: cutover evidence.
- Scope: execute the following cutover sequence.

1. Block new writes to the cohort.
2. Drain accepted in-flight writes.
3. Back up v1 and save its SHA-256.
4. Execute the rehearsed conversion.
5. Check the account ID set.
6. Check each field against the mapping rules.
7. Switch reads to v2.
8. Open each account's preferences page and check the display.
9. Keep writes paused during a fifteen-minute observation period.
10. Disable the cohort's v1 entry points if parsing errors remain at zero.
11. Resume v2 writes.
12. Save and read back a new preference.
13. Configure the v1 backup retention period.

- Acceptance
  - [ ] All parent integration acceptance criteria pass.
  - [ ] Cutover evidence identifies the actual tool version.
  - [ ] Cutover evidence links to the passed recovery rehearsal.

### Failure and recovery boundaries

- Before resuming v2 writes
  - Stop cutover if any consistency check fails.
  - Stop cutover if parsing errors occur during observation.
  - Keep writes blocked until rollback finishes.
  - Switch reads back to the v1 backup.
  - Verify its SHA-256 matches the backup.
  - Confirm all ten accounts can read their original preferences.
  - Resume v1 writes after checks pass.
- After resuming v2 writes
  - Pause cohort writes if read or write verification fails.
  - Drain accepted writes.
  - Save the latest v2 data.
  - Perform forward repair using the rehearsed runbook.
  - Confirm new preferences accepted before the failure remain readable.
  - Resume v2 writes after verification passes.
  - Do not overwrite the latest data with the old v1 backup at this stage.

### Dependencies and new requirements

- Actual cutover waits for the recovery rehearsal because evidence of data preservation after failure is missing.
- Backup waits for write blocking and in-flight draining to obtain a complete cutover baseline.
- Resuming writes waits for consistency checks and observation to pass before ending the safe rollback window.
- Actual cutover and recovery cannot operate on the same cohort simultaneously.
- This case keeps conversion and recovery rehearsal in one sub-issue because they share the same snapshots and cutover state.
- A new requirement to keep writes available during cutover changes the original plan.
  - The requirement decision-maker first confirms adoption.
  - After adoption, create research work to determine how to preserve incremental data.
  - Research acceptance requires recovery evidence sufficient to select an approach.
  - Update the parent's cutover commitment after adoption.
  - Pause actual cutover until the adopted approach passes rehearsal.
  - Retain the original scope if the change is not adopted and the original plan remains valid.
- Create a separate migration issue for another account cohort.
  - Define the new cohort's data set.
  - Reverify data conditions.
  - Preserve this cohort's original acceptance.

## Recommendations and project policy

- Recommendations
  - Investigation delivers usable decision evidence.
  - Sub-issue completion does not replace parent integration acceptance.
  - The parent reviewer determines completion after checking the original commitment and integration evidence.
  - Decompose by outcome boundaries, not arbitrary file counts.
- Formatting policy for this version
  - Basis: [Writing rules](writing.md).
  - Use checkboxes for acceptance.
  - Use native issue mentions for related issues in Linear.
  - Adapt examples to the receiving project's policy.
