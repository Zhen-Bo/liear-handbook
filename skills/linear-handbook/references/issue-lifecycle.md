# Issue lifecycle and closure

Update work in response to observable events so status matches actual delivery.
The workflows below are recommendations.
Linear feature facts appear under “Platform behavior,” with official sources.

## Entry points

- [Progress comment](../assets/templates/progress-comment.md): record new findings and results.
- [Project update](../assets/templates/project-update.md): summarize changes to overall delivery.
- [Handoff](../assets/templates/handoff.md): provide inputs needed to resume execution.
- [Documentation placement](documentation.md): choose the authoritative artifact location.

## Map existing statuses first

1. Read the target Team's status list.
2. Check each status's settings.
   - ID.
   - Category.
   - Usage description.
3. Choose existing statuses using the semantics below.
4. Read automations that change status.
5. Record the mapping in the environment policy; use that Team's IDs for actual updates.

| Work meaning | Mapping |
| --- | --- |
| Not scheduled for execution | Choose an existing backlog-category status |
| Scheduled but not started | Choose an existing unstarted-category status |
| Being executed | Choose an existing started-category execution status |
| Under review or acceptance | Prefer the existing status for that stage; confirm it remains in the started category |
| Blocked on required input | Prefer the existing blocking policy; record real blockers separately in relations |
| Delivered and completion criteria passed | Choose an existing completed-category status |
| Decision to stop pursuing this outcome | Choose an existing canceled-category status |
| Duplicate work consolidated into a canonical issue | Use the native duplicate operation; the system applies the dedicated Duplicate status in the duplicate category |

- If review or acceptance has no dedicated status, use a started status that represents unfinished work.
  - Record the current stage in the body.
  - Identify the reviewer in the review or acceptance record.
- If blocking has no dedicated status, keep an unfinished status matching the actual stage.
  - Put issue blockers in blocked by relations.
  - Put external input gaps in the body's blocking section.
- Statuses with the same name can have different IDs.
  - Resolve the mapping again after changing Teams.
- If a completed-category status is named “Awaiting acceptance,” clarify the existing policy first.
  - Do not apply the completed category while required acceptance remains unmet.

## Events and updates

### 1. Starting work

- Trigger: an executor starts work on a defined outcome.
- Fields
  - Status: map to a started-category execution status.
  - Assignee: confirm the outcome owner.
  - Parent: confirm this item's relation to the overall delivery.
- Body
  - Check this delivery's scope.
  - Confirm completion criteria are determinable.
  - Add required artifact locations.
- Records
  - Add a comment when there is a new finding or decision.
  - Use the status change alone to express starting work.

### 2. Blocked

- Trigger: missing required input prevents a specific operation from continuing.
- Fields
  - Issue blocker: set blocked by in the correct direction.
  - Status: map to an unfinished stage under the blocking policy.
  - Due date: adjust only when the delivery date has been decided again.
- Body
  - Gap: which input is needed.
  - Impact: which delivery cannot continue.
  - Unblocking condition: which result allows work to resume.
  - Responsible person: who can supply the input.
- Records
  - Record the new blocker and evidence in a comment.
  - Update the project when the overall date or scope is affected.
- Resumption
  1. Read the blocker's current result.
  2. Verify that the required input is actually usable.
  3. Update the body's current stage.
  4. Handle the resolved blocker according to current relations and environment policy.

If a blocker is canceled or marked duplicate, follow the replacement artifact and reassess.
A change in how the relation appears does not establish that the input is available.

### 3. Review

- Trigger: an artifact version is ready to assess.
- Fields
  - Status: map to the review stage.
  - Artifact relation: link the reviewed version or PR.
- Body
  - Current approach: update to the version submitted for review.
  - Review entry point: provide the version and necessary context.
- Records
  - In a review request already authorized for sending, state what the recipient needs to assess.
  - Record specific differences when review feedback requires changes.
  - Map back to execution when revision starts.

Assignee expresses outcome ownership.
Name the reviewer separately in the review request.

### 4. Acceptance

- Trigger: the artifact is ready to check against each completion criterion.
- Fields
  - Status: retain the corresponding unfinished acceptance stage.
- Body
  - Acceptance checkboxes: check only results supported by evidence.
  - Verification entry point: link the tested version.
  - Failed items: preserve actual differences.
- Records
  - Verification records identify the test environment.
  - Each result includes an evidence location.
  - After failure, determine what needs repair.

Passed PR review can support a code-review criterion.
Product behavior acceptance still follows the outcome's completion criteria.

### 5. Completion

- Trigger: all currently effective required completion criteria pass.
- Before closure
  1. Check that the delivered artifact matches the tested version.
  2. Confirm required acceptance results.
  3. Confirm the successor can open the artifact.
  4. Check linked parent/sub-issue closure behavior.
  5. Confirm follow-up work has its required inputs.
- Fields
  - Status: map to the completed category.
- Body
  - Consolidate usable artifacts.
  - Update the currently adopted conclusions.
  - Preserve limitations that affect use.
- Records
  - List delivered outcomes in the completion comment.
  - Link verification results to evidence.
  - Provide entry points for any follow-up work.
- After writing
  - Read back this item's status.
  - Check affected parent or sub-issues.
  - Correct the stage if required work was closed prematurely.

### 6. Cancel

- Trigger: a decision has been made to stop pursuing this outcome.
- Before acting
  - Confirm the cancellation decision and its scope.
  - Check work depending on this outcome.
  - Check GitHub PRs that may close as a consequence.
- Fields
  - Status: map to the canceled category.
  - Relations: update dependencies when replacement work exists.
- Body
  - Cancellation reason: record the adopted decision.
  - Remaining impact: explain how downstream work must adjust.
  - Existing artifacts: preserve entry points that remain useful.
- Records
  - Record the cancellation reason in a closure comment.
  - Use native issue mentions for successor work.
- After writing
  - Read back the cancellation result.
  - Confirm affected PR statuses.
  - Confirm required downstream outcomes have a continuation path.

Cancellation expresses a requirement decision.
Handle short-term blocking through the blocking workflow.

### 7. Reopen

- Trigger: new evidence invalidates original completion criteria, or the cancellation decision changes.
- Choose the original or a new issue
  - A gap in the original promise: reopen the original issue.
  - A new requirement beyond the completed promise: create related work with independent completion criteria.
- Fields
  - Archived: restore through the platform first.
  - Status: map to the next actual unfinished stage.
  - Assignee: confirm the successor owner.
  - Relations: check affected parent and dependent work.
- Body
  - Add the new evidence invalidating the original judgment.
  - Correct effective completion criteria or results.
  - Preserve outcomes that remain valid.
- Records
  - Explain the reopening reason in a comment.
  - Provide the next executable action in the handoff record.
- If the original item is a duplicate
  - First confirm whether the canonical issue still owns the same outcome.
  - Confirm how the current interface removes an incorrect duplicate relation.
  - Read back the relation and status after correction.

### 8. Duplicate issues

- Trigger: two issues own the same outcome and one is sufficient for tracking.
- Operation order
  1. Choose the canonical issue.
  2. Compare both outcomes and completion criteria.
  3. Compare evidence unique to the duplicate and incorporate required written conclusions into the canonical issue.
  4. Confirm the canonical issue's successor can read required sources.
  5. Check linked GitHub PR closure behavior.
  6. Use the native duplicate operation from the duplicate issue to the canonical issue.
  7. Read back Duplicate status and the canonical relation.
  8. Check attachments moved to the canonical issue.
  9. Check customer requests moved to the canonical issue.
  10. Check synced Slack threads moved to the canonical issue.
  11. Confirm downstream relations and affected PRs.
- Body
  - Preserve the consolidation reason in the duplicate.
  - Point to the canonical issue with a native issue mention.
  - Summarize effective requirements in the canonical issue.
- Records
  - Record the necessary information added by this consolidation in a comment.
  - Keep original evidence locations traceable.

The native duplicate operation moves specific data; see L08.
Before acting, confirm that the canonical issue's access scope is suitable for that data.
Update stale artifact references after the move.

If work overlaps only partly and each item has an independent delivery, retain both and explain the shared outcome.
Do not substitute a general related relation for a confirmed duplicate operation.

## Define completion criteria by delivery

- Research document
  - Answers the agreed question.
  - Conclusions have traceable evidence.
  - The successor can read the document.
- Deliverable code change
  - Agreed behavior verification passes.
  - Required code review passes.
  - The delivered version is identifiable.
- Work that includes production release
  - The specified version is successfully deployed to the target environment.
  - Required production verification passes.
  - Target users can access the outcome.
- Parent
  - Each required outcome has evidence.
  - Integration acceptance passes.
  - The impact of canceled or duplicate sub-issues has been checked.

If a separate issue owns deployment, close the implementation issue against its own completion criteria.
The deployment issue retains responsibility for production delivery.
Changing the completion boundary of work that originally included launch requires a scope decision and a successor entry point.

## Examples

These fictional demonstrations use tabletop checks to explain the decisions.

### PR merged but acceptance failed

- Original promise: users can export all filtered data.
- Available evidence
  - The PR is merged.
  - Acceptance output contains 100 records; 200 were expected.
- Handling
  1. Record the actual count difference in the body.
  2. Map work to the actual repair stage.
  3. Check whether PR automation set completed prematurely.
  4. Locate the omission through investigation and fix it.
  5. Reverify that all 200 records appear exactly once.
- [x] Merge evidence and behavioral acceptance are assessed separately.
- [x] Failure evidence supports keeping the work unfinished.
- [x] The next step can investigate the difference.

### Partial completion

- Original promise: support CSV and XLSX export.
- Available evidence
  - CSV passes the agreed acceptance.
  - Large XLSX file generation fails.
- Continuing within the original scope
  - Preserve the CSV artifact entry point in the body.
  - Keep XLSX unfinished.
  - Keep the original issue open at its actual stage.
- If staged delivery is adopted
  1. Record the scope adjustment decision and reason.
  2. Define an independent XLSX outcome and completion criteria.
  3. Update the relation between both work items.
  4. Preserve the overall export promise in the parent.
  5. Close CSV against its revised completion criteria.
- [x] The partial success has an artifact entry point.
- [x] Required remaining work has conditions for continuation.
- [x] Parent acceptance preserves the overall promise.

## Platform behavior

Verified on: 2026-09-13.
All sources below are published by Linear.
The evidence level is review of official documentation.

- L01: [Issue status](https://linear.app/docs/configuring-workflows#configure)
  - Section: Configure.
  - Teams can customize status names.
  - Status category ordering is fixed.
- L02: [Duplicate issue status](https://linear.app/docs/configuring-workflows#duplicate-issue-status)
  - Section: Duplicate issue status.
  - The system manages Duplicate status.
  - It is applied automatically when marking an issue duplicate.
- L03: [Issue relations](https://linear.app/docs/issue-relations#duplicate)
  - Section: Duplicate.
    - Point from the duplicate to the canonical issue.
    - The issue displays an entry point back to the canonical issue.
  - Section: [Blocked / blocking](https://linear.app/docs/issue-relations#blocked-blocking).
    - Once a blocker is resolved, the relation appears under Related.
- L04: [GitHub](https://linear.app/docs/github#workflow-automation)
  - Section: Workflow automation.
    - PR events can update issue status according to Team settings.
  - Section: [Magic words](https://linear.app/docs/github#magic-words).
    - Closing relations apply merge-time status automation.
    - Non-closing relations do not apply the merge-time status.
    - Relation syntax creates only a relation.
  - Section: [Automatic PR Cancellation](https://linear.app/docs/github#automatic-pr-cancellation).
    - Directly canceling an issue or marking it duplicate closes open PRs linked by Closes or Contributes.
    - A PR linked to another open issue stays open.
    - PRs linked only by reference stay open.
    - Completing an issue does not close PRs.
    - Automated cancellations do not close PRs.
- L05: [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues#status-automation)
  - Section: Status automation.
  - Teams can enable automatic parent closure when all sub-issues are Done.
  - Teams can enable automatic closure of remaining sub-issues when the parent is Done.
  - Status changes triggered by Git integrations also follow these settings.
- L06: [Delete and archive issues](https://linear.app/docs/delete-archive-issues#auto-close)
  - Section: Auto-close.
    - Issues can be configured to close automatically after inactivity.
    - Changing status can reopen automatically closed items.
  - Section: [Restore issues](https://linear.app/docs/delete-archive-issues#restore-issues).
    - Archived issues can be restored.
- L07: [Releases](https://linear.app/docs/releases#overview)
  - Section: Overview.
  - Done status does not necessarily mean delivery to users.
- L08: [Project Slack channels — Issue duplicates](https://linear.app/changelog/2026-05-21-project-slack-channels#issue-duplicates)
  - Published: 2026-05-21.
  - Section: Issue duplicates.
  - Duplicate uses a dedicated status type.
  - Every duplicate must point to the original issue.
  - Marking an issue duplicate moves customer requests to the original issue.
  - Synced Slack threads move to the original issue.
  - Attachments move to the original issue.
  - When the original issue is completed, synced Slack threads receive notifications.
  - Related Zendesk or Intercom customer tickets reopen.

## Confirm before adoption

- Team status semantics
  - Check actual categories and descriptions.
  - Resolve IDs before assigning names.
- Linked closure behavior
  - Check PR automations.
  - Check parent and sub-issue settings.
  - Use representative work to confirm actual update results.
- Duplicate recovery
  - The cited official sources do not list the complete removal steps.
  - Before using the current UI or tools, confirm the operations to remove the relation and restore status.
- Artifact access
  - Check required evidence readability using the successor's role.
- Automation and acceptance disagree
  - Correct work status based on the outcome first.
  - Have an authorized settings maintainer adjust the trigger policy.
  - Read back the correction using a representative event.
