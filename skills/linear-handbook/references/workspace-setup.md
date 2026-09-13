# Workspace initialization and takeover

Applies to: individual developers with multiple Agents.
Verification date: 2026-09-13.

The following checklists and minimal configuration are usage recommendations.
Feature facts come from official documentation; source locations appear at the end.
Fill the environment record with actual values from the target Workspace.

## Setting purposes and minimal configuration

### Team

- Feature facts: [Teams](https://linear.app/docs/teams).
  - Creating a Workspace produces a Team with the same name.
  - A Team contains issues.
  - A Team can use its own workflow.
- Purpose
  - Establish where issues belong.
- When to adopt
  - Select a Team when starting to track issues.
  - Consider another Team when an independent workflow is needed.
  - Consider another Team when different access boundaries are needed.
- Minimal configuration
  - Reuse the default Team.
  - Save the Team's actual identifiers.
  - See [Object relationships](object-model.md) for modeling multiple products.

### Issue status

- Feature facts: [Issue status](https://linear.app/docs/configuring-workflows).
  - Workflows are configured by Team.
  - Default statuses, in order:
    - Backlog
    - Todo
    - In Progress
    - Done
    - Canceled
  - Status names can be customized.
  - Status-category ordering is fixed.
  - At least one status remains in each category.
  - The system manages Duplicate when work is marked duplicate.
- Purpose
  - Express the current work stage.
- When to adopt
  - Map status meanings before execution.
  - Add a status only when review needs a separate board column.
- Recommended minimal configuration
  - Preserve the default workflow.
  - Reuse existing names and corresponding IDs.
  - Use the started category for review and acceptance stages.
  - Use the completed category only after completion criteria pass.
  - See [Lifecycle](issue-lifecycle.md#map-existing-statuses-first) for mapping.

### Priority

- Feature facts: [Priority](https://linear.app/docs/priority).
  - Priority is optional.
  - Native options are fixed:
    - No priority
    - Low
    - Medium
    - High
    - Urgent
  - Setting Urgent notifies the Assignee.
- Purpose
  - Express urgency.
- When to adopt
  - Use it to decide which work to handle first.
- Recommended minimal configuration
  - Keep No priority when no ordering judgment exists yet.
  - Reuse existing Priority policy.
  - Without a policy, record each item's urgency reason before deciding its level.
  - Express date commitments separately with due dates.

### Estimate

- Feature facts: [Estimates](https://linear.app/docs/estimates).
  - Estimates describe work size or complexity.
  - They are enabled at Team level.
  - The Team chooses the scale.
  - Project effort statistics use Estimates.
  - Cycle effort statistics use Estimates.
  - Zero differs from unestimated.
  - Unestimated work counts as 1 point by default; settings can change this.
- Purpose
  - Compare work size.
  - Help plan capacity.
- When to adopt
  - Enable when the scale can be used consistently and capacity is reviewed regularly.
- Recommended minimal configuration
  - Leave disabled initially in a blank environment.
  - Reuse the scale in an existing environment.
  - The team agrees on what estimate values mean.

### Labels

- Feature facts: [Issue labels](https://linear.app/docs/labels).
  - Labels can belong to a Workspace.
  - Labels can be limited to a specific Team.
  - Label groups provide one level of grouping.
  - An issue can select at most one label per group.
- Purpose
  - Categorize work.
  - Support filtering or routing.
- When to adopt
  - Create labels for recurring classification needs.
- Recommended minimal configuration
  - Reuse existing labels first.
  - Leave empty when there is no classification need.
  - Put only concepts shared by all Teams at Workspace level.
  - Distinguish identically named labels by scope and ID.
  - See [Issue work types](issue-types.md) for type selection.

### Permissions and Agent identity

- Feature facts
  - All users on the Free plan are Admins.[Members and roles](https://linear.app/docs/members-roles)
  - Team owner is a Business/Enterprise feature.[Members and roles](https://linear.app/docs/members-roles)
  - Team owners can restrict administration of Team settings.[Members and roles](https://linear.app/docs/members-roles)
  - Guests access only Teams they were added to.[Members and roles](https://linear.app/docs/members-roles)
  - Guest is a Business/Enterprise feature.[Members and roles](https://linear.app/docs/members-roles)
  - Private Teams are a Business/Enterprise feature.[Private teams](https://linear.app/docs/private-teams)
  - Native delegation can retain a human Assignee.[Assign and delegate issues](https://linear.app/docs/assigning-issues)
  - A delegated Agent must have target Team access.[Assign and delegate issues](https://linear.app/docs/assigning-issues)
- Purpose
  - Confirm visibility scope.
  - Confirm who can modify data or settings.
- When to adopt
  - Check when taking over an environment.
  - Check when adding members.
  - Check when connecting an Agent.
- Recommended minimal configuration
  - Save a contact point for the settings administrator.
  - Give the executor permissions needed for this work.
  - Record the human owner and Agent identity separately.
  - Store credentials in existing secret storage; environment records retain only the access entry point.
  - See [Integration capabilities](agent-tool-capabilities.md#permissions-plans-and-identities) for API/MCP permission judgments.

### Notifications

- Feature facts: [Notifications](https://linear.app/docs/notifications).
  - Notifications can be viewed in the Linear Inbox.
  - Account settings control other channels.
  - Issue subscriptions determine which work is followed.
  - Actual notifications follow personal preferences.
  - Status changes includes several event types; ordinary status changes cannot be selected alone.
- Purpose
  - Remind owners of work requiring attention.
- When to adopt
  - Confirm subscriptions when taking responsibility for work.
  - Configure external channels when timely responses are needed away from Linear.
- Recommended minimal configuration
  - Review Inbox regularly.
  - Subscribe to issues you own.
  - When immediate reminders are needed, have the account owner choose a channel they will check.
  - Agents read the issue's current content on takeover; notifications are only prompts.

## Native settings and tool operations

- Native settings entry points
  - Team name: Team settings → General.[Teams](https://linear.app/docs/teams)
  - Team identifier: Team settings → General.[Teams](https://linear.app/docs/teams)
  - Time zone: Team settings → General.[Teams](https://linear.app/docs/teams)
  - Status: Team settings → Issue statuses.[Issue status](https://linear.app/docs/configuring-workflows)
  - Estimates: Team settings → General → Estimates.[Estimates](https://linear.app/docs/estimates)
  - Labels: Workspace or Team settings → Labels.[Issue labels](https://linear.app/docs/labels)
  - Member roles: Settings → Administration → Members.[Members and roles](https://linear.app/docs/members-roles)
  - Team administrative permissions: Team settings → Access and permissions.[Members and roles](https://linear.app/docs/members-roles)
  - Notifications: Settings → Account → Notifications.[Notifications](https://linear.app/docs/notifications)
- Operators
  - A person with permission or an authorized UI Agent changes settings.
  - The account owner decides personal notification preferences.
- Tool operations
  - Inspect the current tool declarations first.
  - Query the target Team.
  - Query that Team's statuses.
  - Query available labels.
  - Resolve display names to actual IDs.
  - Update issue fields within authorization.
  - Read back target fields and check the write result.
- Missing interface or permissions
  - Record the specific operation that cannot be completed.
  - Point to the corresponding native settings entry point.
  - Have an operator with permission handle it.
  - Refresh mappings after obtaining the result.

See the [integration capability matrix](agent-tool-capabilities.md#capability-matrix) for evidence boundaries of tool capabilities.

## Blank-environment initialization checklist

Follow this order.

- [ ] The Workspace is identifiable.
  1. Create the Workspace in the native interface.
  2. Confirm the plan.
  3. Save Workspace identifiers.
- [ ] The Team is usable.
  1. Select the default Team.
  2. Confirm the time zone.
  3. Save Team identifiers.
- [ ] Status mapping matches work stages.
  1. Read statuses.
  2. Fill the environment record by category.
  3. Confirm the default status.
  4. Check automations that could close work prematurely.
- [ ] Priority has adoption criteria.
  1. Confirm whether a policy already exists.
  2. Record the chosen approach using this page's recommendations.
- [ ] The use of Estimates is explicit.
  1. Determine whether capacity management is needed.
  2. Decide whether to enable Estimates.
  3. If enabled, record the scale and all scoring settings.
- [ ] Labels support actual classification needs.
  1. Review existing labels.
  2. Select labels with a purpose.
  3. Record each label separately.
- [ ] The execution identity can access target work.
  1. Record the owner.
  2. Confirm Agent identity and connection method.
  3. Read the target Team using the execution identity.
- [ ] The owner has a notification entry point.
  1. Have the account owner confirm notification preferences.
  2. Confirm subscription on the first real work item.
- [ ] Fields on the first real work item match the configuration.
  1. Create an issue according to authorized requirements, or enter [Project planning](project-planning.md).
  2. Read back the issue.
  3. Compare each field with the environment record.
  4. Correct actual differences.

## Existing-environment takeover checklist

- [ ] This scope matches current decisions.
  1. Read environment policy.
  2. Read the target issue.
  3. Read the parent.
  4. Read the latest discussion.
- [ ] Identifiers remain valid.
  1. Confirm the current Workspace.
  2. Confirm the target Team.
  3. Query all pages of relevant lists.
  4. Update stale mappings with actual IDs.
- [ ] Status mapping matches the existing workflow.
  1. Read status categories.
  2. Check each name's purpose.
  3. Confirm the default status.
  4. Compare one representative issue with the [lifecycle](issue-lifecycle.md).
- [ ] Automation effects can be assessed.
  1. Review auto-close settings.
  2. Review auto-archive settings.
  3. Review parent closing behavior.
  4. Review sub-issue closing behavior.
  5. If Cycle or Git integrations exist, record each status-transition rule.
- [ ] Optional fields follow existing policy.
  1. Review Priority criteria.
  2. Review the Estimate scale.
  3. Check label purposes.
  4. Have the administrator clarify identically named items or unclear purposes.
- [ ] Operational scope matches current responsibility.
  1. Read the target issue using the execution identity.
  2. Confirm deliverables can be opened.
  3. Check the settings administrator.
  4. Check available tools.
- [ ] The owner can follow the work.
  1. Confirm subscription.
  2. Have the account owner check notification preferences.
- [ ] The takeover record is reusable.
  1. Save the verification date.
  2. Fill the environment record.
  3. Record actual differences affecting operations.
  4. Read back fields after the first authorized write.
  5. Check that existing object IDs were used.

## Environment record

Fill this structure in the target Workspace's existing policy document.
Read every ID from the target environment.

- Verification date:
- Operator:
- Workspace
  - Name:
  - URL:
  - ID:
  - Plan:
  - Settings administrator:
- Team
  - Name:
  - Identifier:
  - UUID:
  - Time zone:
  - Access scope:
  - Settings administrator:
- Status (one group per work stage)
  - Work stage:
  - Name:
  - ID:
  - Category:
- Default status:
- Automation (one group per rule)
  - Trigger event:
  - Result:
  - Settings entry point:
- Priority usage criteria:
- Estimates
  - Enabled:
  - Scale:
  - Extended scale:
  - Allow zero:
  - Unestimated score:
- Label (one group per label)
  - Name:
  - ID:
  - Scope:
  - Team ID:
  - Group:
  - Purpose:
- Execution identity
  - Human Assignee:
  - Agent identity:
  - Connection method:
  - Team access:
  - Available operations:
- Notifications
  - Viewing entry point:
  - Subscription rules:
- Actual differences (one group per difference)
  - Difference:
  - Affected operation:
  - Handler:
  - Resolution condition:
- First real work entry point:
- Readback evidence:

## Sources and verification

All publishers are Linear.
All verification dates are 2026-09-13.
Evidence status: "confirmed in documentation".
Section names can be located with in-page search.

- [Teams](https://linear.app/docs/teams)
  - Overview: default Team.
  - Team settings: settings entry point.
- [Issue status](https://linear.app/docs/configuring-workflows)
  - Overview: default workflow.
  - Configure: statuses and categories.
  - Default status: initial status of new issues.
  - Duplicate issue status: system-managed duplicate status.
  - Auto-close and auto-archive: closing and archiving automation.
- [Priority](https://linear.app/docs/priority)
  - Overview: fixed levels.
  - Urgent Notifications: Urgent alerts.
- [Estimates](https://linear.app/docs/estimates)
  - Overview: purpose.
  - Configure: Team scale.
  - Zero estimates: scoring zero and unestimated work.
  - Analytics: effort statistics.
- [Issue labels](https://linear.app/docs/labels)
  - Labels: scope.
  - Label groups: grouped-selection restrictions.
  - Create labels: creation entry point.
- [Members and roles](https://linear.app/docs/members-roles)
  - Overview: role-management entry point.
  - Admin: all Free users are Admins.
  - Team owner: Team settings administration.
  - Guest: restricted access.
- [Private teams](https://linear.app/docs/private-teams)
  - Overview: plan conditions.
- [Assign and delegate issues](https://linear.app/docs/assigning-issues)
  - Delegating to agents: human responsibility and Agent access.
- [Notifications](https://linear.app/docs/notifications)
  - Overview: Inbox.
  - Configure: channel settings.
  - Subscribing to an issue: subscription.
