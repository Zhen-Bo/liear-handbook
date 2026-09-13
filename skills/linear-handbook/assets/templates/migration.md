# Migration issue body template

For switching data or usage workflows to a new state.
Classification: [Work type guide](../../references/issue-types.md#migration).

## Instructions

- Required fields
  - Old and target states.
  - Affected scope.
  - Mapping rules.
  - Cutover sequence and entry criteria.
  - Consistency checks.
  - Recovery triggers and operations.
  - Recovery verification evidence.
  - Conditions for retiring the old system.
  - Acceptance criteria.
- Optional fields
  - Notification arrangements for affected parties.
  - Phased cutover schedule.

### Recommendations

1. Copy the body below and replace every placeholder.
2. Clearly distinguish this batch from later batches.
3. Specify a verifiable passing threshold for every cutover step.
4. Describe how new data written after cutover will be handled.
5. Choose rollback or forward repair based on reversibility.
6. After completion, add cutover and recovery verification evidence.

- The recovery plan must have the agreed verification evidence.
- This template's cutover and recovery thresholds are handbook recommendations.
- The adopting team sets acceptable downtime.
- The adopting team sets data retention periods.

## Copyable body

```markdown
## Goal and scope

- Old state: `<Current system>`.
- Target state: `<System after migration>`.
- Batch scope: `<Users or dataset>`.
- Mapping rules: `<How old values become new values>`.

## Cutover

1. `<Entry checks and passing thresholds>`.
2. `<Perform conversion and handle writes>`.
3. `<Consistency checks and passing thresholds>`.
4. `<Switch traffic or user entry points>`.

## Recovery

- Trigger: `<Threshold for stopping or recovering>`.
- Recovery method: `<Rollback or forward repair>`.
- Operation entry point: `<Runbook or command>`.
- New data handling: `<How to preserve writes made after cutover>`.
- Verification evidence: `<Rehearsal method and success criteria>`.

## Old system retirement

- Retirement conditions: `<Observation period and results>`.
- Method: `<Scope to disable or remove>`.
- Retention requirements: `<Data retention period and cleanup timing>`.

## Acceptance criteria

- [ ] This batch is operating in the target state.
- [ ] Consistency checks meet the agreed thresholds.
- [ ] The recovery plan passes the agreed verification.
- [ ] The old system has been handled according to this issue's retirement conditions.
- [ ] Outputs and verification evidence have been added.
```

## Completed example: Convert test account preferences to the new format

The following is a pending issue in a fictional project.
Commands and paths are examples.
This example pauses writes during maintenance to prevent loss of new data during rollback.

```markdown
## Goal and scope

- Old state: Ten internal test accounts use preferences-v1.json.
- Target state: The same accounts use preferences-v2.json.
- Batch scope: The ten accounts listed in migration/cohort.txt.
- Mapping rule: theme=dark becomes appearance=dark.
- Mapping rule: theme=light becomes appearance=light.
- Mapping rule: An unset theme becomes appearance=system.
- Mapping rule: Preserve original values in all other fields.

## Cutover

1. Rehearse conversion and rollback in the test environment using a copy of this batch's data.
2. Confirm that the copy's SHA-256 after rollback matches its value before conversion.
3. Pause preference writes for this batch, confirm that all entry points block new writes, and drain accepted writes still in flight.
4. Back up the v1 files and save a SHA-256 manifest.
5. Run python scripts/migrate_preferences.py --cohort migration/cohort.txt.
6. Confirm that the ID sets for the ten accounts match exactly.
7. Check each account's appearance value against the mapping rules.
8. Confirm that all other fields exactly match their original v1 values.
9. Switch this batch's read entry points to v2 and open each account's preferences page to check the display.
10. Keep writes paused for a fifteen-minute observation period and confirm zero parsing errors.
11. Disable this batch's v1 read entry points and resume v2 writes.

## Recovery

- Trigger: Any consistency check fails before writes resume.
- Trigger: A parsing error occurs during the fifteen-minute observation period.
- Recovery method: Switch this batch's read entry points back to the v1 backup.
- Operation entry point: python scripts/restore_preferences.py --cohort migration/cohort.txt.
- New data handling: Keep writes paused throughout the rollback window.
- Post-rollback check: All ten accounts can read their original preferences.
- Post-rollback check: File SHA-256 values match the backup manifest.
- Post-rollback action: Resume v1 writes.
- Failure after resuming v2 writes: Pause writes, preserve the latest v2 data, and repair forward through the incident response workflow.
- Rehearsal evidence: migration/rehearsal.md records the checks above.

## Old system retirement

- Retirement condition: This batch passes consistency checks.
- Retirement condition: Zero parsing errors during the fifteen-minute observation period.
- Method: Disable this batch's v1 read entry points.
- Retention requirement: Retain the v1 backup for seven days for investigation.
- Cleanup timing: Existing backup retention rules remove it on expiration.

## Acceptance criteria

- [ ] All ten accounts read preferences from v2.
- [ ] ID sets match exactly.
- [ ] Field mapping checks pass.
- [ ] SHA-256 checks in the rollback rehearsal pass.
- [ ] Zero parsing errors occur during observation.
- [ ] This batch's v1 entry points are disabled.
- [ ] One preference can be saved and read back after v2 writes resume.
- [ ] Backup retention is configured.
- [ ] Cutover records and rehearsal evidence have been added.
```

## Linear feature basis

Verified on: 2026-09-13.

- A Standard template can prefill the issue body. [Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates)

## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
