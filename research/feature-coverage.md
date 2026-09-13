# Linear feature coverage and adoption guide

Verified: 2026-09-12.
Context: an individual developer with multiple Agents.
Research baseline: [scope-and-sources.md](scope-and-sources.md); object selection: [object-model.md](object-model.md); project policy: [AGENTS.md](../AGENTS.md).

## Feature matrix

Purpose and limitation columns record facts from official documentation; importance is this handbook’s recommendation.
“Core” means the first version must address the problem; “conditional adoption” means configuring a feature when the need arises; “extension” means reserving an interface and a decision point.
Sections and evidence status for sources from “Search” through “Billing and plans” appear at the end.

| Feature | Purpose and behavior | First-version importance and context (recommendation) | Permission and plan limits | Sources |
| --- | --- | --- | --- | --- |
| Search and views | Global Search searches issue bodies and comments; search within a view matches only IDs/titles. Custom Views save dynamic filters | Core: check duplicates before creation, find work before execution, periodically review stalled work | Search returns at most 500 results. Sharing a view URL does not grant access; Initiative views require Enterprise. Feature pages do not explicitly state minimum plans for general search or issue/project views | [Search](https://linear.app/docs/search), [Custom Views](https://linear.app/docs/custom-views) |
| Triage | A Team inbox for reviewing work from external teams or integrations before admitting it into the workflow; excluded from ordinary views by default | Intake handling is core; enable Triage when external intake exists. An individual can initially review an existing backlog manually | Must be enabled in Team settings; Team Settings Management controls configuration permissions. Intelligence, Rules, and Responsibility require Business/Enterprise; the minimum plan for basic Triage needs confirmation | [Triage](https://linear.app/docs/triage), [Members and roles](https://linear.app/docs/members-roles) |
| Feedback | Customer Requests links feedback to issues/projects while preserving sources; ordinary team email intake creates issues but does not notify senders of later updates | Core: source → duplicate check → adopted conclusion → issue. Adopt Customer Requests conditionally; evaluate Asks for bidirectional intake | Customer Requests explicitly lists Free/Basic/Business/Enterprise and requires admin enablement; integrations have separate plan limits. Asks and Intercom/Zendesk integrations are listed under Business. Guests cannot see Customer Requests, consistent across FAQ and roles documentation | [Customer Requests](https://linear.app/docs/customer-requests), [Create issues](https://linear.app/docs/creating-issues), [Pricing](https://linear.app/pricing), [Members and roles](https://linear.app/docs/members-roles) |
| Templates | Standard issue templates prefill content and properties; form templates can require fields. Project templates can include milestones and issues | Core: reuse outcome, scope, and acceptance structure. Add Project templates for repeated project patterns | Workspace issue templates cannot preset team-specific statuses/labels; Team templates apply to that team. Team Template Management can restrict management to team owners; minimum plans for each template type are not explicit | [Issue templates](https://linear.app/docs/issue-templates), [Project templates](https://linear.app/docs/project-templates), [Members and roles](https://linear.app/docs/members-roles) |
| Recurring work | Recurring issues create subsequent work by due date and cadence; original template updates do not propagate to a recurrence | Conditional adoption: maintenance has a fixed cadence and a determinable result each time | Documentation describes creating the next issue at 00:01 on the day after the due date in the team’s time zone; creation is not completion-triggered. The feature page does not specify a minimum plan or recurrence-specific role matrix | [Create issues](https://linear.app/docs/creating-issues) |
| Analytics | Insights calculates Issue count, Cycle Time, Lead Time, and other metrics from the current view; archived issues can be included | Extension: use for concrete questions about trends across periods. Start with views to review pending and blocked work | Insights requires Business/Enterprise; Cycle Time plots only completed issues that passed through in progress, and Lead Time includes only completed items. Retain sampling conditions and visibility scope | [Insights](https://linear.app/docs/insights) |
| Notifications | Inbox receives notifications; individuals configure Desktop, Mobile, Email, Slack, and issue subscriptions | Core: owned work and blocking relationships need a review entry point; subscribe only to views requiring action | Account settings and browser/system permissions affect delivery. Notification categories group multiple events and cannot be split arbitrarily. The feature page does not specify a minimum plan | [Notifications](https://linear.app/docs/notifications), [Custom Views](https://linear.app/docs/custom-views) |
| Import and export | Dedicated importers or CLI map external data to Linear; CSV supports analysis and record retention | Conditional adoption: legacy-system takeover, data handoff, or external analysis; select necessary data first | Import requires workspace admin and source permissions. Workspace issue CSV export requires admin, or owner on Enterprise. View exports allow 250 issues for members and 2,000 for admins/Enterprise owners; guests cannot export issues. CSV excludes attachment files; minimum plans need confirmation | [Importing guidance](https://linear.app/docs/import-issues), [Exporting Data](https://linear.app/docs/exporting-data) |
| Archiving | Auto-close closes stale work; Auto-archive moves closed issues into the archive after inactivity conditions are met; archived issues can be restored | Core: understand closure, archiving, and deletion. Adopt automation conditionally so cleanup does not replace acceptance | Issue archiving is automated, with no manual archive option. Parent/sub-issues, active cycles, and unfinished projects can delay archiving; Team settings permissions are restricted. Deleted issues have only a 30-day recovery period; the minimum plan is not explicit | [Delete and archive issues](https://linear.app/docs/delete-archive-issues), [Members and roles](https://linear.app/docs/members-roles) |

## Adoption and follow-up workflows

These are workflow design recommendations for subsequent work; assess check results against actual data.

| Core or conditional item | Trigger and input | Expected result after checking | Follow-up work |
| --- | --- | --- | --- |
| Search and views | Preparing an issue or reviewing a stalled backlog | Search bodies, comments, and relevant archived work; link an existing issue and explain the relationship. Save filters with clear purposes such as intake, stalled work, or closure review | Duplicate/stalled-work checks in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md); view permissions in the [environment inventory](../skills/linear-handbook/references/workspace-setup.md) |
| Triage | External feedback or an integration creates an issue | Confirm the problem, duplicates, and owner, then accept into the workflow, link a duplicate, or record rejection reasons. If waiting for information, define a trackable return condition; explicitly include Triage status in the view | Intake checks in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md); enablement and configuration permissions in the [environment inventory](../skills/linear-handbook/references/workspace-setup.md) |
| Feedback | A source message or Customer Request arrives | Preserve a locatable source; attach to existing work before deciding on a new verifiable issue. Update the body with the adopted conclusion; separately confirm reply recipients and sending authorization | Feedback flow in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md); product operations in [collaboration and operations extensions](extension-model.md) |
| Templates | Similar issues repeatedly lack necessary information | Add necessary questions to a standard template; use forms only for inputs required at creation. Follow AGENTS.md with acceptance checkboxes and numbered completed items | Type selection in the [issue types guide](../skills/linear-handbook/references/issue-types.md); native configuration in the [environment inventory](../skills/linear-handbook/references/workspace-setup.md) |
| Recurring work | Stable maintenance work has an owner | Specify cadence, team time zone, completion criteria per occurrence, and schedule maintainer; check whether unfinished previous work requires rescheduling; update recurrence content directly | Maintenance cadence in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md) |
| Analytics | A specific question such as “which work waits longest?” | Record date range, statuses, and archive inclusion before interpreting charts; completion counts and Cycle Time do not prove quality, deployment, or user acceptance | Maintenance metrics in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md); broader operations analytics in [collaboration and operations extensions](extension-model.md) |
| Notifications | Handoff, blocking, or waiting for someone else | Confirm issue subscriptions and handling responsibility; subscribe to specific statuses through views as needed. Read Inbox items and delivered email are not acceptance evidence | Review entry points in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md); Agent-readable notification interfaces in [tool capability research](agent-tool-capabilities.md) |
| Import and export | Taking over an existing tool or preserving handoff data | Select sources and samples first; compare counts, statuses, parent relationships, comments, and attachment readability. Check missing fields in the importer’s specific documentation before choosing a full migration | Takeover inventory in the [environment inventory](../skills/linear-handbook/references/workspace-setup.md); storage locations in the [documentation guide](../skills/linear-handbook/references/documentation.md) |
| Archiving | Periodic review of overdue and closed work | Determine status from delivery evidence before checking auto-close/auto-archive conditions; preserve closure reasons and result links. Restore archived work before editing | Closure in the [issue lifecycle](../skills/linear-handbook/references/issue-lifecycle.md); backlog maintenance in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md) |

Project writing policy comes from AGENTS.md: bodies maintain current conclusions, comments preserve new findings, and work records describe actual results only.
These are user policies; “core” classifications in the matrix are research recommendations.

## Plans and research gaps

- Plan baseline: Pricing explicitly lists Free with 2 teams/250 issues, Basic with 5 teams/unlimited issues, and Business/Enterprise with unlimited teams/issues. [Pricing](https://linear.app/pricing)
- Permission baseline: Free members automatically become admins; on Business/Enterprise, team owners can restrict template and team settings management. Feature availability still requires checking the operator’s permissions. [Members and roles](https://linear.app/docs/members-roles)
- The Pricing text extraction did not retain all comparison-table checkmarks. This document treats only explicit plan text as fact and does not infer universal availability for unlabeled features.

| Gap or difference | Current approach and impact | Verification and follow-up |
| --- | --- | --- |
| Actual workspace plan, team access, and administrative permissions | The matrix describes public product capabilities; environment availability must still be assessed before configuration | Read Billing and Team Access and permissions during inventory; the Billing route follows [Billing and plans](https://linear.app/docs/billing-and-plans) |
| Minimum plans for some basic features are not explicit | Search, general views, basic Triage, templates, recurrence, notifications, import/export, and archiving cannot yet have per-plan guarantees | Open the actual plan comparison and feature settings before configuration; if unclear, ask Linear support about the specific feature and plan. Manual intake and document templates remain available before adoption |
| Guest feedback handoff and integration visibility | “Customer Requests” FAQ and “Members and roles” Guest sections both explicitly exclude Guest access to Customer Requests; the restriction is consistent | Confirm Guest access to issues, attachments, and external integrations before configuration; Customer Requests cannot be the only handoff entry point |
| Customer Requests FAQ plan table omits Basic | FAQ text explicitly includes Basic, but the integration table does not fully represent it. Assess core Customer Requests and integration availability separately | For a specific Basic integration, read its own documentation and settings; do not infer support from the core feature |
| Recurrence behavior when previous work is unfinished, and Agent-manageable fields | Documentation establishes time-triggered creation, insufficient to guarantee non-overlap; native UI functionality does not establish MCP operations | Check the next occurrence’s relationship to unfinished work with a controlled sample; verify API/MCP capabilities and readback |
| Import completeness and CSV coverage as a recovery source | Field mappings vary by source; CSV lacks attachments and cannot promise complete workspace restoration | Read the specific importer documentation during migration; sample comments, attachments, and relationships; choose artifact storage using the documentation guide |
| Auto-archive timing and settings location | “Delete and archive issues” uses both Workflows & automations and Issue statuses & automations; changes generally take effect on the next run within 24 hours | Record the actual settings entry point and periods during inventory; interpret delays from related-work statuses. Sources did not establish whether archived issues are excluded from Free allowances, so archiving is not an allowance workaround |

## Source records

All 15 sources below are published by Linear and were verified on 2026-09-12.
Page-level publication/update dates were not confirmed; evidence status is “documented.”
Section names support in-page searching; Guest handoff checks and minimum-plan gaps appear above.

| Title and URL | Sections / supported conclusions | Limitations |
| --- | --- | --- |
| [Search](https://linear.app/docs/search) | Search workspace, Search specific views, Q&A; search scope and result limit | Native search interface, not an MCP search specification |
| [Custom Views](https://linear.app/docs/custom-views) | Page introduction, Create views, Copy view link, Issue view subscriptions | Initiative view plan threshold is explicit; URLs do not grant access |
| [Triage](https://linear.app/docs/triage) | Configure, Automation, FAQ; intake, advanced features, exclusion from views | Requires Team enablement; advanced features vary by plan |
| [Customer Requests](https://linear.app/docs/customer-requests) | Configure, Add requests, FAQ; feedback links and plans | FAQ explicitly excludes Guests; verify specific Basic integrations separately |
| [Issue templates](https://linear.app/docs/issue-templates) | Create standard issue templates, Create form templates | Workspace/team property scopes differ |
| [Create issues](https://linear.app/docs/creating-issues) | Create an issue via email, Create recurring issues | Team time zone and maintenance of existing recurrence content |
| [Insights](https://linear.app/docs/insights) | Page introduction, Apply filters, Select Insights Parameters | Business/Enterprise; automatic sampling conditions affect metrics |
| [Notifications](https://linear.app/docs/notifications) | Configure, Notification timing, Subscribing to an issue, FAQ | Account/channel/system settings affect notifications |
| [Importing guidance](https://linear.app/docs/import-issues) | Page introduction, Choose an import method, Understand the import process | Requires admin; data mappings vary by source importer |
| [Exporting Data](https://linear.app/docs/exporting-data) | Workspace CSV exports, Issue view CSV exports | Role and record-count limits; no attachment files |
| [Delete and archive issues](https://linear.app/docs/delete-archive-issues) | Delete issues, Auto-close, Auto-archive, Restore issues | Relationship and timing conditions; differing settings path names |
| [Pricing](https://linear.app/pricing) | Free, Basic, Business, Enterprise plan cards | Dynamic plans; text extraction does not fully preserve checkmarks |
| [Members and roles](https://linear.app/docs/members-roles) | Admin, Team owner, Member, Guest | Plans, workspace restrictions, team management permissions |
| [Project templates](https://linear.app/docs/project-templates) | Overview, Create templates | Workspace/team template availability differs |
| [Billing and plans](https://linear.app/docs/billing-and-plans) | Manage your billing | Entry point for confirming the actual plan |

## Verification and handoff

1. Compared all nine feature categories against official pages; each matrix row includes purpose, importance, permissions/plans, and sources.
2. Mapped every category to a concrete follow-up workflow; unknown rules have impacts and verification methods.
3. Cross-checked Team, Project, and Issue scope against object-model.md.

- [x] Official documentation conclusions and first-version recommendations are separate.
- [x] All 15 sources have locatable sections, verification dates, and limitations.
- [x] Documentation differences and pre-adoption gaps are included.
- [x] Search, notifications, exports, and archiving do not substitute for delivery acceptance evidence.

Use this document’s triggers, inputs, and results in the [maintenance checklist](../skills/linear-handbook/references/maintenance.md).
Use the gap table to arrange verification when actual configuration is needed.
