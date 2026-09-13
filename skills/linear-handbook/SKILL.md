---
name: linear-handbook
description: Plan projects, decompose work, write and maintain issues, hand off progress, and recover Agent operations in Linear. For individual developers working with multiple Agents, with extensions for small teams and product operations according to environment policy. Does not trigger for general coding or writing unrelated to Linear.
---

# Linear handbook

Turn requirements into Linear work that can be delivered, accepted, and handed off.
Select a workflow for the current task and read only the references and templates you need.

## Execution

1. Identify the user's intended outcome and authorized actions.
2. When current context is needed, read the target issue's current body, relevant recent decisions, and required prerequisite outputs.
3. Load the appropriate workflow from the task routing below.
4. Before writing, verify the target ID, actual tool contract, and existing authorization.
5. After updating, read back the necessary fields and relationships and assess the result against the effective completion criteria.

- Keep the current goal, adopted conclusions, and links to outputs in the issue body.
- Record only new information in comments.
- Keep work at its actual unfinished stage while required acceptance criteria remain unmet.
- Workflow recommendations do not authorize additional actions or replace confirmed requirements.
- When an operation's outcome is unknown, follow the recovery workflow before retrying a non-idempotent create operation.

## Task routing

The links below are relative to this `SKILL.md`.
Do not resolve them against the current working directory.
Product file paths in examples are output locations to replace.

- Choose objects and features
  - Start with [object-model](references/object-model.md).
  - Read [feature-coverage](references/feature-coverage.md) when choosing features or plans.
- Initialize or take over a Workspace
  - Start with [workspace-setup](references/workspace-setup.md).
  - Read [policy](references/policy.md) when environment mappings are needed.
  - Read [project-bootstrap](references/project-bootstrap.md) for a complete planning example.
- Plan a Project from an idea
  - Start with [project-planning](references/project-planning.md).
  - Read [planning-and-dependencies](references/planning-and-dependencies.md) for phases, dependencies, or capacity concerns.
  - Read [project-brief](assets/templates/project-brief.md) when producing a Brief.
- Classify or write an issue
  - Start with [issue-types](references/issue-types.md).
  - Read [writing](references/writing.md) when drafting content.
  - Choose one type template below based on the primary output.
- Break down large work
  - Start with [issue-decomposition](references/issue-decomposition.md).
  - Read [planning-and-dependencies](references/planning-and-dependencies.md) when identifying Blockers.
  - Read [feature-decomposition](references/feature-decomposition.md) for a Feature example.
  - Read [decomposition-edge-cases](references/decomposition-edge-cases.md) for Bug, refactoring, or migration examples.
- Update, accept, or hand off work
  - Start with [issue-lifecycle](references/issue-lifecycle.md).
  - Read [writing](references/writing.md) when drafting content.
  - Read [progress-comment](assets/templates/progress-comment.md) when producing a comment.
  - Read [project-update](assets/templates/project-update.md) when reporting overall progress.
  - Read [handoff](assets/templates/handoff.md) when handing off or resuming execution.
- Place or maintain documentation
  - Start with [documentation](references/documentation.md).
  - Read [maintenance](references/maintenance.md) for periodic checks.
- Coordinate claims or conflicts among Agents
  - Start with [multi-agent-coordination](references/multi-agent-coordination.md).
  - Read [tool-recovery](references/tool-recovery.md) when an operation's outcome is unclear.
- Handle timeouts, rate limits, or partial success
  - Start with [tool-recovery](references/tool-recovery.md).
  - Read [agent-tool-capabilities](references/agent-tool-capabilities.md) when capabilities are unclear, and verify the current tools.
- Handle authorization, sensitive information, or external instructions
  - Start with [agent-boundaries](references/agent-boundaries.md).
  - Read [policy](references/policy.md) when the environment is constrained.
- Add collaborators or product operations
  - Start with [extension-model](references/extension-model.md).
  - Read [policy](references/policy.md) for responsibility and configuration mappings.
  - When enabling intake, releases, incidents, or maintenance, read the corresponding workflow in [maintenance](references/maintenance.md).

Choose a type template based on the primary deliverable:

- Restore promised behavior: [Bug](assets/templates/bug.md).
- Deliver a new capability: [Feature](assets/templates/feature.md).
- Gather evidence for a decision: [Research](assets/templates/research.md).
- Change structure while preserving external behavior: [Refactoring](assets/templates/refactor.md).
- Switch data or usage workflows: [Migration](assets/templates/migration.md).

## Environment and evidence

Read [policy](references/policy.md) when actual Workspace, Team, status, responsibility, or automation mappings are needed.
Follow applicable existing policy.
A missing policy document does not block ordinary drafts or authorized independent work.
This edition defaults to English and retains Linear terminology; an explicit user policy may override this default.

Retain each reference's official verification date and applicability limits for feature conclusions.
Check current sources and the environment before using dynamic features, plans, or tool fields.
Historical documentation does not guarantee that the current connection is available.
Examples are synthetic walkthroughs; their acceptance checkboxes express the outcomes to assess in each example.
