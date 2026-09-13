# Backlog maintenance and ongoing operations checklist

Context: an individual developer with multiple Agents.
Original feature verification date: 2026-09-12.

Use this guide to decide which work needs attention and when a maintenance pass can end.
The workflow and time budgets are first-version recommendations.

- Feature evidence: [feature coverage research](feature-coverage.md).
- Writing and body maintenance policy: [writing rules](writing.md).
- Document placement and maintenance: [documentation.md](documentation.md).

## Maintenance cadence

The developer names the owner of the maintenance pass; Agents perform authorized checks and updates.
Choose the question to answer before deciding scope and time budget.

- Event triggers
  - When new feedback arrives, review relevant items at the start of the next work session.
  - When a commitment date approaches, check whether the remaining work can finish.
  - When a blocker clears, reassess executable scope.
  - Handle faults that continue to affect users immediately through the incident process.
- Weekly review
  - Suggested budget: about 20 minutes.
  - Start with work in progress.
  - Check committed deliverables.
  - Check dependencies affecting other work.
- Monthly review
  - Suggested budget: about 30 minutes.
  - Check whether long-standing backlog items remain valid.
  - Check whether recurrence matches capacity.
  - Check documents needed for the current work.
  - Review affected areas earlier when product direction or settings change.

- [ ] Selected items have a disposition.
- [ ] Actionable items have an owner and next step.
- [ ] Waiting items have return conditions.
- [ ] When time runs out, remaining scope and continuation entry points are saved.

End the check when there is no new evidence or decision.
An ordinary cleanup time budget does not end incident response responsibility.

## Start and write back

1. Confirm operator permissions and the authorized write scope.
2. Read the current target issue body.
3. Review recent comments and deliverables.
4. Check the actual effect of blockedBy on the current operation.
5. Select the Team or Project review scope.
6. Set status and date filters for the current question.
7. Confirm the entry point covers waiting work, including applicable Triage queues. [Triage](https://linear.app/docs/triage)
8. Reread the target before writing and merge new changes from people or Agents.
9. Put new information in the locations below.
10. Read back the changed content and relationships.

- Body: currently effective goals and adopted conclusions.
  - Add deliverable entry points.
  - Retain open questions and affected operations.
- Comment: findings or decision reasons that add information.
- Project update: changes affecting Project commitments.

- [ ] Deliverable entry points open successfully.
- [ ] Issue mentions point to the correct work.
- [ ] Status matches delivery evidence.

When an operation's outcome is unknown, read back before deciding to retry.
Team workflows can have custom status names; choose by the meaning of existing statuses. [Issue status](https://linear.app/docs/configuring-workflows)
Set blockedBy only for actual prerequisites.
If a prerequisite issue is still open, first check whether its inputs are already usable.
See the [lifecycle guide](issue-lifecycle.md#map-existing-statuses-first) for status mapping and event updates.

## Maintenance checklist

### Intake and Triage

- Triggers
  - New feedback arrives.
  - New Triage items appear.
  - A request for information reaches its return date.
  - An intake review starts.
- Inputs
  - Original source.
  - Affected scenario.
  - Existing issue.
  - Triage queue.
  - Snoozed queue.
- Exit criteria
  - Selected items have a destination.
  - Requests for information have an owner and return time.

- [ ] Every intake item has a clear disposition.
  1. Check duplicates using “From feedback to issue.”
  2. When accepting, add an assessable problem and next step.
  3. Record missing information when details are insufficient.
  4. Assign responsibility and a return time for that information.
  5. Retain rejection reasons.
  6. When snoozing, confirm the return date and visibility scope.

- Triage can accept new work. [Triage](https://linear.app/docs/triage)
- Duplicates can link to existing work. [Triage](https://linear.app/docs/triage)
- Unwanted items can be declined. [Triage](https://linear.app/docs/triage)
- Snoozed items return at the chosen time or when new activity occurs. [Triage](https://linear.app/docs/triage)
- Ordinary views exclude Triage by default. [Triage](https://linear.app/docs/triage)
- Snoozed items are hidden from other users by default. [Triage](https://linear.app/docs/triage)

Without Triage, manually review the existing intake entry point.
Temporarily leaving the queue does not mean processing is complete.

### Stalled work

- Triggers
  - An agreed update or delivery time passes.
  - Dependencies change.
  - In-progress work lacks a next step.
- Inputs
  - Recent deliverables and activity.
  - Assignee.
  - BlockedBy.
  - Commitment date.
  - Executor handoff information.
- Exit criteria
  - Work can continue.
  - Remaining blockers have resolution owners and return conditions.
  - Work that no longer serves the goal is passed to the stale-work review.

- [ ] Another session can pick up the cause of the stall and the next step.
  1. Open the deliverables first to check whether progress merely needs to be recorded.
  2. Identify missing decisions or inputs.
  3. Confirm permissions and execution capacity.
  4. Identify affected acceptance criteria.
  5. Add valid deliverables and an owner for the next step.
  6. Reassess executable scope when prerequisite deliverables are usable.
  7. Retain unmet criteria for partially completed work.

The last update time alone does not establish a lack of progress.
If a PR is merged but deployment or acceptance evidence is missing, continue tracking according to the issue's delivery definition.

### Duplicate work

- Triggers
  - Preparing to create an issue.
  - Processing feedback.
  - Finding potentially duplicate work.
- Inputs
  - Problem context.
  - Expected outcome.
  - Acceptance criteria.
  - Original source.
  - Candidate issues.
- Exit criteria
  - The same work is consolidated into one authoritative issue.
  - Distinct work has clear outcomes and relationships.

- [ ] Duplicate handling preserves the original requirements and traceable entry points.
  1. Search by context or outcome terms.
  2. Also search the exact error message when available.
  3. Read candidate issue bodies and comments.
  4. Check closed and archived work when needed.
  5. Compare the problem and acceptance scope.
  6. Once duplication is confirmed, merge new evidence and valid requirements into the authoritative issue first.
  7. Check GitHub PR relationships and dependencies on other work.
  8. Confirm automatic PR closure falls within the current authorization.
  9. Confirm the canonical issue's access scope is appropriate for transferred data.
  10. Use the available native duplicate operation.
  11. Read back the duplicate relationship and actual status.
  12. Read back linked PR statuses.
  13. Check attachments moved to the canonical issue.
  14. Check customer requests moved to the canonical issue.
  15. Check synced Slack threads moved to the canonical issue.
  16. Update deliverable references after transfer.

- Related work is not necessarily duplicate work.
- Prerequisite dependencies are not duplicates.
- Compare delivery scope before treating platform variants as duplicates.
- If the tool cannot mark duplicates, retain candidates and the specific follow-up action.

- Workspace Search searches bodies and comments. [Search](https://linear.app/docs/search)
- Search within a view matches only ID/title. [Search](https://linear.app/docs/search)
- Narrow the scope and search again when the 500-result limit is reached. [Search](https://linear.app/docs/search)
- Duplicate uses a system-managed status; changing an ordinary status alone does not create a duplicate relationship. [Issue status](https://linear.app/docs/configuring-workflows)

### Stale work and archiving

- Triggers
  - Monthly backlog review.
  - Changes to requirements or product direction.
  - A due date has passed.
  - Automatic closure or archiving differs from expectations.
- Inputs
  - Original rationale.
  - Current impact.
  - Delivery evidence.
  - Dates.
  - Parent and sub-issues.
  - Project and Cycle.
  - Automation settings.
- Exit criteria
  - Valid work has an adjusted plan.
  - Delivered work is completed according to evidence.
  - Obsolete work has a cancellation reason.
  - Open decisions have owners.
  - Archiving delays are explained or have verification work assigned.

- [ ] Each cleanup candidate is handled according to current value and delivery evidence.
  1. Decide whether the work remains necessary or has become obsolete.
  2. Check for existing deliverables.
  3. Update commitments and next steps for valid work.
  4. Before canceling obsolete work, check GitHub PR relationships and other dependencies.
  5. Confirm automatic PR closure falls within current authorization.
  6. Update the obsolete work's body conclusion and record the cancellation reason.
  7. After cancellation, read back issue and linked PR statuses.
  8. Add deliverable and verification entry points for delivered work.
  9. Check auto-close inactivity conditions.
  10. Check auto-archive time and relationship conditions.
  11. Restore archived work before editing it.

- A long period without updates is only a review signal.
- Automatic closure does not establish acceptance.
- Cleanup does not authorize deleting data.

- Auto-close uses inactivity periods. [Delete and archive issues](https://linear.app/docs/delete-archive-issues)
- The platform runs auto-archive; there is no manual archive option. [Delete and archive issues](https://linear.app/docs/delete-archive-issues)
- Unfinished related work or an active Cycle can delay archiving; compare official conditions with actual settings. [Delete and archive issues](https://linear.app/docs/delete-archive-issues)

### Project health

- Triggers
  - Weekly review.
  - A Milestone or delivery commitment changes.
  - A critical issue becomes blocked.
- Inputs
  - Current delivery goal.
  - Milestones.
  - Dates.
  - Critical dependencies.
  - Deliverables and acceptance evidence.
  - Latest Project update.
- Exit criteria
  - Health reflects current delivery commitments.
  - Risks to commitments have response owners and a next decision point.

- [ ] Delivery evidence and remaining risks support the health assessment.
  1. Confirm whether the next delivery remains achievable.
  2. Check the critical path and missing decisions.
  3. Record necessary goal or date changes.
  4. Update deliverable entry points.
  5. When a material change occurs, the Project lead summarizes an update and links related issues.

Native Project updates provide the following health indicators with explanatory text. [Initiative and Project updates](https://linear.app/docs/initiative-and-project-updates)
The interpretations below are this guide's recommendations.

- On track: current evidence supports meeting the commitment.
- At risk: a specific risk may prevent meeting the commitment.
- Off track: work has already diverged from the commitment and needs an adjusted approach or goal.

Completion percentages do not replace acceptance.
Update reminders are review entry points; write an update when there is new information.

### Recurring work and document validity

- Triggers
  - Monthly review.
  - Prior maintenance remains unfinished.
  - A template changes.
  - Plans or tool capabilities change.
  - A deliverable link breaks.
- Inputs
  - Recurrence schedule.
  - Team time zone.
  - Previous and next occurrences.
  - Template.
  - Authoritative document entry points.
  - Named document maintainer.
  - Document purpose and applicable version.
- Exit criteria
  - The schedule matches execution capacity.
  - Overlapping work has clear owners.
  - Required authoritative documents are readable.
  - Obsolete content has a handling owner and replacement entry point.

- [ ] The schedule continues to support actual work.
  1. If the prior occurrence is unfinished, determine whether the next one duplicates it.
  2. Decide whether to adjust cadence based on capacity.
  3. Confirm cadence and due dates.
  4. Confirm the Team time zone.
  5. Confirm each occurrence's deliverables.
  6. Inspect the recurrence directly when revising its content.
- [ ] Documents support the next action.
  1. Open the authoritative full text needed for the current work.
  2. Confirm intended readers can access it.
  3. Check the applicable version and named maintainer.
  4. Compare duplicate full texts against the authority declaration and merge valid additions into the authoritative version.
  5. Correct obsolete sections or identify affected operations and follow-up work.
  6. Date and version any historical snapshots that must be retained.
  7. Link other reading entry points back to the current version.

Recurring issues are expected to create the next occurrence at 00:01 on the day after the due date in the Team time zone. [Create issues](https://linear.app/docs/creating-issues)
Later edits to the source template do not propagate to an existing recurrence. [Create issues](https://linear.app/docs/creating-issues)
Check actual generation behavior with unfinished prior work under “Checks before adoption.”
See [documentation.md](documentation.md#updates-and-invalidation) for obsolete-document handling.

## From feedback to issue

1. Preserve a locatable source and its original meaning.
2. Record the affected context and expected outcome.
3. Search for existing issues using the duplicate-work checklist.
4. Add feedback for the same outcome to existing work; create a new issue only for an independently verifiable outcome.
5. Separate new evidence from recommendations and identify the currently adopted decision.
6. Assign decision responsibility and return conditions when a necessary choice remains open.
7. Update the body with the current adopted conclusion.
8. Retain reasons or process details that add information in comments.
9. If shared rules are affected, the document maintainer updates the authoritative full text.
10. Link deliverable entry points back to the issue.
11. Update the health assessment when Project commitments are affected.
12. Read back the body and source relationships.

Preserve content and structure when the user supplies a complete replacement.
When notifying the person who gave feedback, confirm the recipient and message, then act within existing authorization.

- Customer Requests can link feedback to an issue or Project. [Customer Requests](https://linear.app/docs/customer-requests)
- Integration sources can retain links to original messages. [Customer Requests](https://linear.app/docs/customer-requests)
- Without that feature, source links support the same flow.
- Ordinary Team email intake does not send intake or closure notifications to the sender. [Create issues](https://linear.app/docs/creating-issues)

## Release and incident management

The first version serves products with existing deployment and monitoring methods.
Follow the product's established operational rules.

### Before release

- Trigger: a batch of changes is planned for release.
- Inputs
  - Version and change scope.
  - Acceptance results.
  - Deployment method.
  - Observation metrics.
  - Rollback entry points.
- [ ] Required inputs for a safe release are available.
  1. Open delivery evidence.
  2. Confirm the release executor.
  3. Assign observation responsibility and a time window.
  4. Confirm failure handling.
  5. If required inputs are missing, record the blocker and pause the release step.
- Extensions
  - Multi-environment approval.
  - Formal change windows.
  - Cross-team release coordination.
  - Native Releases integration.

### After release

- Triggers
  - Deployment completes.
  - The observation window ends.
  - An anomaly appears.
- Inputs
  - Deployment records.
  - Actual version.
  - Verification of core operations.
  - Monitoring results.
- [ ] Release results provide sufficient evidence to assess delivery.
  1. Record the release.
  2. Record verification results.
  3. Close the issue only when its delivery definition is met.
  4. Route anomalies through the incident process.
  5. Link remaining improvements to trackable work.
- Extensions
  - Automated release pipelines.
  - Gradual rollout.
  - Cross-service rollback strategies.

### Incident intake and response

- Trigger: a fault continues to affect users.
- Inputs
  - Discovery time.
  - Impact scope.
  - Known evidence.
  - Existing runbook.
  - Responder.
- [ ] Recovery evidence and observation responsibility are established, allowing recovery monitoring to begin.
  1. Name a coordinator.
  2. Agree on the next update time.
  3. Prioritize containing user impact.
  4. Record significant actions and results.
  5. Add recovery evidence and assign observation responsibility.
- Extensions
  - Formal severity levels.
  - On-call.
  - Paging.
  - SLO/SLA.
  - External status page.

### Incident recovery and improvement

- Trigger: impact is resolved and observation is complete.
- Inputs
  - Recovery evidence.
  - Timeline.
  - Evidence status of the cause.
  - Remaining risks.
- [ ] Incident outcomes and permanent improvements each have traceable deliverables.
  1. Record recovery verification.
  2. Record the cause and unanswered questions.
  3. Retain unmet criteria in the original work item.
  4. Give independent improvements their own owners and acceptance criteria.
  5. Link follow-up issues back to the incident record.
  6. Name the authoritative location and maintainer for any required postmortem.
- Extensions
  - Cross-team incident command.
  - Formal postmortem review.
  - Improvement tracking across incidents.

## Checks before adoption

- Triage
  - Intelligence, Rules, and Responsibility require Business or Enterprise. [Triage](https://linear.app/docs/triage)
  - Check the actual plan and Team settings before configuration.
  - See [feature coverage research](feature-coverage.md#plans-and-open-questions) for other minimum-plan gaps.
- Recurrence
  1. Keep the prior occurrence unfinished in an authorized controlled sample.
  2. Check the result after the due date.
  3. Check the time zone and fields available for readback.
  4. Use observations to determine cadence and overlap handling.
  5. Check API/MCP management capabilities separately.
- Auto-close/auto-archive
  - Read actual time limits.
  - Check relationship conditions.
  - Review automation outcomes.
  - Assign verification responsibility when settings or evidence are missing.
- Duplicate
  - Duplicate has a dedicated status type. [Project Slack channels](https://linear.app/changelog/2026-05-21-project-slack-channels#issue-duplicates)
  - Duplicate is a system-managed status name applied automatically by the native marking operation. [Issue status](https://linear.app/docs/configuring-workflows)
  - The relationship pointing to the canonical issue establishes duplication.
  - Read back the dedicated status and canonical relationship after the operation.
  - Customer requests move to the canonical issue. [Project Slack channels](https://linear.app/changelog/2026-05-21-project-slack-channels#issue-duplicates)
  - Synced Slack threads move to the canonical issue. [Project Slack channels](https://linear.app/changelog/2026-05-21-project-slack-channels#issue-duplicates)
  - Attachments move to the canonical issue. [Project Slack channels](https://linear.app/changelog/2026-05-21-project-slack-channels#issue-duplicates)
- Automatic GitHub PR closure
  - Directly canceling an issue closes open PRs linked with Closes or Contributes. [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
  - Marking an issue as duplicate has the same effect. [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
  - A PR stays open if it is also linked to another open issue. [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
  - A PR with only a reference relationship stays open. [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
  - Completing an issue does not close the PR. [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
  - Automatic cancellation does not close the PR. [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
- Document and feedback visibility
  - Confirm source access using the intended reader's permissions.
  - Confirm deliverables and authoritative documents are readable.
  - Guests cannot see Customer Requests; provide accessible issue or attachment entry points.
  - This Guest limit follows official sources compared in [feature coverage research](feature-coverage.md#plans-and-open-questions).

## Source records

Publisher: Linear.
Original feature verification date: 2026-09-12.
Evidence status: confirmed in documentation.

- [Triage](https://linear.app/docs/triage)
  - Sections
    - Take actions.
    - Automation.
    - FAQ.
  - Purpose
    - Intake and snooze operations.
    - View exclusions and plan conditions.
  - Limit: confirm Team enablement and actual settings.
- [Search](https://linear.app/docs/search)
  - Sections
    - Search workspace.
    - Search specific views.
    - Q&A.
  - Purpose
    - Search scope and the 500-result limit.
  - Limit: MCP search depends on actual tool capabilities.
- [Delete and archive issues](https://linear.app/docs/delete-archive-issues)
  - Sections
    - Auto-close.
    - Auto-archive.
    - Restore issues.
  - Purpose
    - Time and relationship conditions.
  - Limit: read actual environment settings.
- [Create issues](https://linear.app/docs/creating-issues)
  - Sections
    - Create an issue via email.
    - Create recurring issues.
  - Purpose
    - Email notification behavior.
    - Recurrence scheduling.
  - Limit: verify Agent management capabilities separately.
- [Customer Requests](https://linear.app/docs/customer-requests)
  - Sections
    - Add requests to issues or projects.
  - Purpose
    - Feedback sources and work relationships.
  - Limit: confirm the specific integration and reader visibility.
- [Initiative and Project updates](https://linear.app/docs/initiative-and-project-updates)
  - Sections
    - Overview.
    - Create Initiative and Project updates.
  - Purpose
    - Health indicators and explanatory text.
  - Limit: delivery evidence must still support the health assessment.
- [Issue status](https://linear.app/docs/configuring-workflows)
  - Sections
    - Configure.
    - Duplicate issue status.
  - Purpose
    - Team workflows.
    - System-managed duplicate status.
  - Limit: verify native status and tool response representations separately.

### Additional verification

Verified: 2026-09-13.

- The dedicated duplicate status type in “Project Slack channels” is the adopted basis for classification.
  - “Triage” → Take actions still describes the Canceled type.
  - The 2026-05-21 “Project Slack channels” update explicitly introduces a dedicated type.
- “Issue status” → Duplicate issue status: reread the system-managed Duplicate name.
- [GitHub](https://linear.app/docs/github#automatic-pr-cancellation)
  - Section: Automatic PR Cancellation.
  - Purpose: effects of direct cancellation and duplicate marking on PRs.
  - Limit: check actual PR relationships and other open issues.
- [Project Slack channels](https://linear.app/changelog/2026-05-21-project-slack-channels#issue-duplicates)
  - Published: 2026-05-21.
  - Section: Issue duplicates.
  - Purpose
    - Dedicated duplicate type.
    - Context transfer to the canonical issue.
  - Limit: confirm canonical access scope before transfer.

## Related guidance

- [Lifecycle guide](issue-lifecycle.md): completion criteria and status mapping.
- [Lifecycle reopening rules](issue-lifecycle.md#7-reopen): distinguish gaps in the original commitment from new requirements.
- [documentation.md](documentation.md): authoritative locations and named maintainers.
- [Project update template](../assets/templates/project-update.md): health assessment and overall delivery changes.
- [Document updates and obsolescence](documentation.md#updates-and-invalidation): identify obsolete content and handle historical snapshots.
- [Writing rules](writing.md): issue body and work-record policy.

Start maintenance by reading the target issue's latest content and choosing the current review scope.
When configuring a feature, complete its corresponding “Checks before adoption.”
