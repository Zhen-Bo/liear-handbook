# Extending to team collaboration and product operations

Verified: 2026-09-12.
Context: an individual developer with multiple Agents, gradually extending to a small team and a live product.
Evidence rules: [policy](policy.md#evidence-and-sources).
Object relationships: [object-model.md](object-model.md).
Feature matrix: [feature-coverage.md](feature-coverage.md).

## Adoption

Assess organizational size and operational needs separately.
An individual developer can adopt feedback, release, incident, and maintenance modules once a product is live.
Assign responsibilities and adjust collaboration policy when colleagues join.
This is a handbook design recommendation, extending the research scope's future expansion boundaries.

1. Apply the core rules to each task, identifying outcomes, responsibility, and acceptance evidence.
2. Use the triggers below to select the collaboration or operational capabilities needed.
3. Use environment policy to map actual Teams, statuses, permissions, tools, and responsible people.
4. Verify the configuration and handoff with one representative task before expanding adoption.

“Recommendation” indicates workflow design.
“Documented fact” is limited to product behavior explicitly stated by a source.
See [writing](writing.md) for formatting and maintaining current conclusions.
Explicitly applicable user policies take precedence.

## Four areas of responsibility

- Core rules
  - Define deliverables and completion criteria.
  - Decompose work by outcome.
  - Identify real dependencies.
  - Maintain currently adopted conclusions.
  - Retain usable evidence and handoff entry points.
  - Handbook maintainers own shared rules.
  - Task owners maintain the facts for their work.
- Roles
  - Name the requirements decision-maker.
  - Name the executor.
  - Name the reviewer.
  - Name the person accepting the outcome.
  - Assign release and incident responsibility when operations are enabled.
  - The product or project owner assigns named responsibilities.
- Workspace policy
  - Map shared concepts to the actual environment.
  - Retain object identifiers.
  - Retain status and classification mappings.
  - Record actual permissions.
  - Record scheduling and integration settings.
  - The configuration maintainer owns the effective version.
- Operational modules
  - Customer feedback provides an intake process.
  - Releases retain evidence of delivery to an environment.
  - Incidents cover service recovery.
  - Reliability and recurring maintenance provide ongoing checks.
  - Each enabled module has a named maintainer.

The core uses semantic work stages; policy supplies actual status IDs.
This version loads references on demand from a single entry point.

## Roles and handoffs

These are process responsibilities; one person may hold several roles.
The names do not represent native Linear permission types.

- Requirements and priority
  - The individual developer makes requirement tradeoffs initially.
  - A team names a product or project decision-maker.
  - Retain adopted decisions in the handoff.
  - Retain tradeoff reasons.
  - Retain completion criteria.
- Issue ownership and execution
  - The Assignee owns the outcome.
  - The Agent executes the authorized scope.
  - Retain execution scope in the handoff.
  - Retain current conclusions.
  - Retain deliverable entry points.
  - Record the conditions for clearing actual blockers.
- Review and acceptance
  - The author provides self-check evidence.
  - Arrange a reviewer under policy when independent review is needed.
  - Name the person who accepts the outcome.
  - Retain verification methods in the handoff.
  - Retain results.
  - Retain issues affecting acceptance.
- Configuration maintenance
  - Name a maintainer and confirm their administrative permissions.
  - Record the scope of configuration effects.
  - Record before-and-after differences.
  - Identify affected work.
- Releases and operations
  - Name the owner of each release.
  - Name the incident owner.
  - List a backup when continued coverage is needed.
  - Retain the target environment in the handoff.
  - Retain event impact.
  - Retain recovery evidence.
  - Retain follow-up work entry points.
  - Retain authorized destinations when messages must be sent.

Documented fact: an issue has one Assignee at a time. [Assign and delegate issues](https://linear.app/docs/assigning-issues#overview)
Native delegation retains human responsibility, and the Agent needs access to the Team. [Assign and delegate issues](https://linear.app/docs/assigning-issues#delegating-to-agents)
Check current capabilities to determine whether an external MCP session maps to a native Agent identity.

Documented fact: [Members and roles](https://linear.app/docs/members-roles#role-types) describes roles and plans.

- All Free plan members are Admins.
- Team owner requires Business or Enterprise.
- Guest requires Business or Enterprise.
- Team owners can restrict management of certain settings.

Review responsibility in a workflow does not replace platform access controls.

## Adoption triggers and configuration

The following are recommendations.
Use actual needs as triggers rather than headcount or issue-count thresholds.

- Another member starts sharing delivery work
  - Configuration or policy changes
    - Assign responsibility
      - Assignee.
      - Reviewer.
      - Requirements decision-maker.
    - Add handoff entry points and notification responsibility.
  - Adoption check: the recipient can read the deliverables and determine the next action.

- Work regularly needs a shared time window
  - Configuration or policy changes
    - Define the scheduling cadence and capacity review.
    - Enable Team Cycles when needed.
  - Adoption checks
    - Trial one interval and record unfinished work's next steps separately from release arrangements.
    - Cycles are not tied to Releases.
    - [Cycles](https://linear.app/docs/use-cycles).

- Work areas need different workflows, schedules, or access
  - Configuration or policy changes
    - Evaluate adding a Team.
    - Map the environment
      - Status.
      - Label.
      - Template.
      - Members.
      - Agent access.
      - Integrations.
  - Adoption checks
    - Use a representative issue to check
      - Target settings.
      - Relationships.
      - Member visibility.
    - Then migrate in batches.

- Cross-domain work needs a shared outcome and ongoing coordination
  - Configuration or policy changes
    - Maintain one Project brief and add participating Teams.
    - Give each issue a primary home.
  - Adoption checks
    - Confirm object membership
      - Each issue has one Team.
      - Each issue has at most one Project.
    - Shared deliverables have references and acceptance from each party.
    - [Teams](https://linear.app/docs/teams#tips-on-structuring-teams).
    - [Projects](https://linear.app/docs/projects#add-issues-to-a-project).

- Customer feedback or integrations continuously submit requests
  - Configuration or policy changes
    - Enable the feedback module.
    - Define intake settings
      - Intake owner.
      - Duplicate-check entry point.
      - Processing deadline.
    - Select as needed
      - Triage.
      - Customer Requests.
  - Adoption checks
    - Verify a representative source
      - It reaches the intake queue.
      - Its original source can be located.
      - Processing decisions are traceable.
      - Ownership is clear.
    - Include template overrides of the default Triage status in the checks.
    - [Triage](https://linear.app/docs/triage#create-issues).

- Users begin relying on production
  - Configuration or policy changes
    - Enable release and incident modules.
    - Complete release settings
      - Target environment.
      - Release responsibility.
      - Recovery entry points.
      - Notification policy.
  - Adoption checks
    - A release can be traced to deployment and verification evidence.
    - An incident drill identifies responders and follow-up improvements.

- Backup recovery, dependency updates, or reliability checks become recurring work
  - Configuration or policy changes
    - Enable the maintenance module.
    - Configure maintenance work
      - Cadence.
      - Team time zone.
      - Completion criteria for each occurrence.
      - Maintainer.
  - Adoption checks
    - Check unfinished prior work alongside the new occurrence.
    - Native recurrence creates issues on schedule; template updates do not propagate to existing recurrences.
    - [Create issues](https://linear.app/docs/creating-issues#create-recurring-issues).

- External collaborators need access to only part of the work
  - Configuration or policy changes
    - Confirm external collaboration boundaries
      - Guest/Team access.
      - Shareable deliverables.
      - Integration visibility.
    - Name an internal contact.
  - Adoption checks
    - Use the actual collaborator role to confirm access to
      - Issues.
      - Attachments.
      - Required sources.
    - Customer Requests cannot be a Guest's sole work entry point.
    - [Members and roles](https://linear.app/docs/members-roles#guest).
    - [Customer Requests](https://linear.app/docs/customer-requests#faq).

- Formal audit, organization-wide permissions, or compliance requirements emerge
  - Configuration or policy change: record requirements and open questions under enterprise governance and create separately verifiable research work.
  - Adoption check: identify the requirements owner and decision evidence; see the enterprise governance table.

Teams can configure separate workflows.
Projects can span Teams; an issue belongs to only one Team. [Teams](https://linear.app/docs/teams#tips-on-structuring-teams)
Check plan limits before adding a Team.
Adding an Agent or launching an individual product does not by itself justify splitting Teams.
This choice follows the [feature selection table](object-model.md#feature-selection-table).

## Operational modules

Enable modules according to product needs.
See [maintenance](maintenance.md#release-and-incident-management) for detailed release and incident procedures.

- Customer feedback
  - Input: a locatable source.
  - Input: the problem context.
  - Input: actual impact.
  - The intake owner handles duplicates and requests for missing information.
  - The requirements decision-maker sets priority.
  - Record a decision to adopt, reject, or request information.
  - Provide the corresponding issue entry point.
  - Confirm the recipient and authorization when a response is needed.
  - Check Customer Requests plan eligibility and integration requirements separately. [Customer Requests](https://linear.app/docs/customer-requests#configure)
- Releases
  - Input: verified changes.
  - Input: target environment.
  - Input: an identifiable version.
  - Name the release owner.
  - Retain deployment records.
  - Retain environment verification.
  - Retain recovery instructions.
  - Provide required release notes.
  - Native Releases requires Business or Enterprise. [Releases](https://linear.app/docs/releases#ci-setup)
  - CI setup uses a pipeline access key. [Releases](https://linear.app/docs/releases#ci-setup)
  - An issue can initially link to external CI/CD evidence.
- Incidents
  - Input: an alert or report.
  - Input: affected service.
  - Input: start time.
  - Name the responder.
  - Retain impact and response timelines.
  - Retain recovery evidence.
  - Record evidence of the cause or open questions.
  - Give each follow-up improvement an owner and acceptance criteria.
  - Existing operational tools handle detection and real-time alerts.
  - Follow the applicable runbook for recovery actions.
  - Triage responsibility can use a separately configured rotation source. [Triage](https://linear.app/docs/triage#triage-responsibility)
- Reliability and maintenance
  - Input: scheduled checks or incident improvements.
  - Name the maintainer and check scope.
  - Retain results for each occurrence.
  - Retain exception handling.
  - Link improvement issues.
  - Identify the next check.
  - When using service objectives, record the metric source.
  - Record the measurement window.
  - Record decision thresholds.
  - Recurring issues are optional. [Create issues](https://linear.app/docs/creating-issues#create-recurring-issues)

Even when one person holds several roles, retain implementation, deployment, and acceptance evidence separately.
The Releases documentation distinguishes Done from actual delivery to users. [Releases](https://linear.app/docs/releases#overview)
Before disabling a module, name who takes over unfinished work.
Update event entry points and schedules so work is not routed to an unattended destination.

## Migration example: two collaborators join a live individual product

This is a design example, evaluated by comparing responsibilities, object limits, and deliverable entry points step by step.
Policy values are specific to the example.

### Starting point and goal

- Starting point: one developer and multiple Agents manage a product's frontend and API repositories in one Team.
- Change: the product gains production users.
- A developer and a support collaborator then join.
- Goal: each piece of feedback has an intake owner, each release has production evidence, and another person can pick up every task.
- Assumption: all three collaborators have necessary access to the same Team and share a workflow.
- The migration does not depend on adding Teams or paid operational features.

### Migration steps

1. The individual developer adds feedback entry points, release environments, deployment/monitoring/runbook links, and owners.
   Use ordinary issues to record feedback sources, release evidence, and incident follow-ups manually, making operations usable first.
2. Use “A subscription can be completed in production” as the representative outcome.
   Frontend and API issues in the existing Project provide feature verification; a separate release task records the version, production verification, and recovery entry points.
   Link the deliverables from the Project brief.
3. When colleagues join, explicitly assign each issue's Assignee, current reviewer, and release owner.
   The support collaborator handles duplicate checks and initial intake; the product owner makes tradeoffs.
   Record Agent execution scope and handoff evidence in the work item.
4. Run “The subscription button does not work” through intake.
   Record the source and impact, link the existing fix, and confirm the recipient can read the deliverables.
   After the fix, attach production verification and respond within the authorized scope.
5. Keep the existing Team because all three people share a workflow.
   Evaluate Cycles when fixed scheduling becomes useful.
   Review Triage and Customer Requests as feedback volume grows.
   Evaluate Releases when an environment-based release view is needed.
6. If support later needs independent statuses or an access boundary, evaluate a separate Team.
   First list current mappings and affected objects, then verify target statuses, relationships, visibility, and integrations with one representative issue before changing other work.
   If the trial fails, stop expanding, repair using the saved settings and work mapping, and confirm someone still owns the original workflow.

### Desk review

- [x] All four operational modules can be adopted during the individual stage.
- Step one supplies entry points and responsibility without a headcount threshold.
- [x] Responsibilities are mapped for three-person collaboration.
- Assignee and Agent responsibilities follow “Assign and delegate issues.”
- [x] Each frontend and API issue has one Team and at most one Project.
- The example retains the object limits in “Teams” and “Projects.”
- [x] Steps two and four use production evidence to assess release outcomes.
- Neither a Cycle nor Done substitutes for deployment evidence.
- [x] Paid features have adoption checks.
- Different workflow or access needs trigger a new Team.
- [x] Trial scope, expansion criteria, and failure handling are stated, and a recipient can trace current deliverables.

## Enterprise governance

This section defines future research scope and open questions only.

| Area | Open questions |
| --- | --- |
| Multiple Teams or Workspaces | Who decides organizational boundaries, shared deliverables, data ownership, and cross-environment integrations? How are duplicate sources avoided? |
| Identity and access | Are centralized identity management, offboarding, least privilege, and periodic access reviews needed? What data do features and integrations actually expose? |
| Audit and retention | Which actions and decisions must be retained, for how long, who can read them, and how is integrity verified? |
| Change approval and separation of duties | Which actions require independent review or approval? Which roles cannot be combined? How are emergency changes approved retrospectively? |
| Compliance and data handling | What obligations, sensitive-data classifications, storage locations, and external-processor requirements apply? Who makes the determination? |

## Checks before adoption

- Target Workspace plan, roles, and settings
  - Impact and verification
    - Confirm affected features
      - Additional Teams.
      - Guests.
      - Advanced Triage.
      - Releases.
    - Inventory the actual plan and configuration before choosing native features.

- External Agent identity and capabilities
  - Impact and verification
    - Native delegation requires Team access.
    - Compare the current connector and actual account using agent-tool-capabilities, then read back fields for representative work.

- Release integration triggers
  - Impact and verification
    - The continuous deployment example in “Releases” can create a completed release on a push to main.
    - If deployment runs later, that event does not prove the change is live.
    - Include successful production deployment and verification evidence in the actual workflow.

- Guest feedback handoff and integration visibility
  - Impact and verification
    - The “Customer Requests” FAQ explicitly says Guests cannot see Customer Requests, consistent with “Members and roles.”
    - Provide issues and deliverable entry points Guests can access, and confirm external integration permissions.

- A recurring issue's previous occurrence is unfinished
  - Impact and verification
    - “Create issues” documents time-based creation, which does not guarantee non-overlap.
    - Check due-date and unfinished-work behavior for a representative recurrence before setting the handoff approach.

- Actual data mappings after splitting Teams or roles
  - Impact and verification
    - Documented facts do not cover this Workspace's custom settings.
    - Verify each item with a sample before expanding
      - Status.
      - Labels.
      - Templates.
      - Relationships.
      - Visibility.
      - Integrations.

These are configuration checkpoints.
This document delivers research and design; feature evidence comes from reading official documentation.

## Source records

All nine sources below are published by Linear and were verified on 2026-09-12.
Page-level publication or update dates were not confirmed.
Evidence status: confirmed in documentation.
Section names provide in-page search locations; feature limits and adoption checks appear separately above.

- [Teams](https://linear.app/docs/teams)
  - Sections and supported conclusions
    - Overview.
    - Team settings.
    - Team limits.
    - Tips on structuring teams.
    - Team selection and scope.
  - Applicability: confirm Team limits and edit permissions against the actual plan and policy.

- [Members and roles](https://linear.app/docs/members-roles)
  - Sections and supported conclusions
    - Role types.
    - Admin.
    - Team owner.
    - Guest.
    - Supported conclusions
      - Roles.
      - Permissions.
      - Guest access.
  - Applicability
    - Process responsibilities are not platform roles.
    - Check external integrations individually.

- [Assign and delegate issues](https://linear.app/docs/assigning-issues)
  - Sections and supported conclusions
    - Overview.
    - Delegating to agents.
    - Single Assignee and Agent access.
  - Applicability: check identity mapping for external MCP sessions separately.

- [Triage](https://linear.app/docs/triage)
  - Sections
    - Configure.
    - Create issues.
    - Automation.
    - Triage responsibility.
  - Applicability
    - The three advanced features require Business or Enterprise.
    - Templates can override status.

- [Customer Requests](https://linear.app/docs/customer-requests)
  - Sections
    - Configure.
    - Add requests to issues or projects.
    - FAQ.
  - Applicability
    - Check the feature and integration plans separately.
    - The FAQ explicitly excludes Guest visibility.

- [Releases](https://linear.app/docs/releases)
  - Sections
    - Overview.
    - Status automations.
    - CI setup.
    - Example for continuous deployments.
  - Applicability
    - Business or Enterprise.
    - Match completion events to the actual deployment workflow.

- [Create issues](https://linear.app/docs/creating-issues)
  - Section and supported conclusion: Create recurring issues.
  - Applicability
    - Time-based creation.
    - Original templates and existing recurrences are maintained separately.

- [Cycles](https://linear.app/docs/use-cycles)
  - Sections
    - Page introduction.
    - Configure.
  - Applicability
    - Enabled per Team.
    - Scheduling is separate from releases.

- [Projects](https://linear.app/docs/projects)
  - Sections
    - Overview.
    - Add issues to a project.
  - Applicability
    - A Project can span Teams.
    - An issue belongs to only one Project.

## Workspace policy interface

See [policy](policy.md) for configuration fields, unknown values, and responsibilities.
After enabling an operational module, use the corresponding workflow in [maintenance](maintenance.md).
