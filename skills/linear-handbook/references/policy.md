# Environment policy

Map common workflows to the actual working environment.
This document defines the configuration contract; values come from user-designated policy or information confirmed for the current task.

## Resolve policy

1. Find the policy explicitly designated by the user and applicable to the target product, Team, or repository.
2. Verify its scope, effective version, and maintainer.
3. When policies conflict within the same scope, identify the current conclusion from effective instructions and explicit versions.
4. Use current tools to verify IDs, permissions, and automation needed for this operation.
5. If a missing value affects a specific operation, first complete independent drafting or reading, then ask for that missing information.

When there is no policy document, use confirmed information to complete the necessary mappings.
Ordinary drafts do not require every setting to be filled in first.
Never substitute example names or IDs for target data.

## Field contract

| Field | Content | When to load |
| --- | --- | --- |
| Policy identity | Scope, version, maintainer, and source | When adopting a policy |
| Environment | Names and IDs of Workspace, Team, and Project | When reading or writing the corresponding objects |
| Workflow | Status meaning, category, ID, and completion criteria | When changing status |
| Responsibility | Assignee, executor, decision-maker, reviewer, and acceptance reviewer | When claiming, assigning, or handing off work |
| Classification and inputs | Labels, templates, and intake entry points | When classifying or creating work |
| Scheduling | Cycle, WIP, review capacity, time zone, and session granularity | When scheduling or decomposing work |
| Writing | Explicit overrides for language, formatting, and completion criteria | When drafting outputs |
| Capabilities | Plan, role, scope, tool interface, and verification date | When a required operation is constrained |
| Automation | GitHub, parent, sub-issue, and scheduling rules | When an operation may trigger related changes |
| Operations | Enabled modules, environments, and runbook entry points | When the corresponding module is enabled |
| Notifications | Recipients, synchronization destinations, and authorized scope | When sending external messages |

For initialization fields, see [Environment record in workspace-setup](workspace-setup.md#environment-record).
Credentials are managed by the execution environment.
Policy retains only necessary access entry points.

## Work granularity and authorization

- "Use a sub-issue for each session" can be an adopter's preferred work granularity.
  - When the user directly assigns ordinary work, carry out that original request.
  - Do not split additional issues or wait for a new issue merely to satisfy this preference.
- Assess parent completion through overall acceptance.
- Existing authorization continues within its original scope.
- Policy cannot authorize external operations the user has not authorized.
- When new side effects exceed authorization, prepare a concrete proposal according to [agent-boundaries](agent-boundaries.md).

## Evidence and sources

1. Cite official pages and sections that directly support feature conclusions.
2. Retain the verification date.
The verification date does not replace the publication date.
3. Use a fixed commit and file location for code evidence.
4. Tool declarations support only that interface's fields and contract.
5. Operational observations support only the tested environment, account, version, and operation.
6. Explicitly identify inferences and design recommendations.

- Conflicting sources
  - First compare whether the feature, date, version, plan, and interface match.
  - Check specific official documentation and update articles.
  - When testing is needed, limit it to the smallest authorized scope.
  - If the difference remains unresolved, retain it and identify the affected operations.
- Unconfirmed capabilities
  - Verify current tool schemas and target access.
  - Do not treat native UI features as callable MCP capabilities.
  - Do not treat an unsuccessful search as evidence of nonexistence.

## Maintenance

This skill directory is the effective source for workflows and templates.
Installed copies retain the full internal structure.
After updating the effective source, maintainers deliver a complete version.
Return fixes in distributed copies to the effective source, then regenerate the copies.
Keep environment policy in the user-designated location; skill updates do not overwrite it.
When users maintain their own installed copy, compare and preserve their changes before updating.
