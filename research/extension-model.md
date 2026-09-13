# Extension boundaries for team collaboration and product operations

Verified: 2026-09-12.
Context: an individual developer with multiple Agents, gradually extending to a small team and a live product.
Research baseline: [scope-and-sources.md](scope-and-sources.md); object relationships: [object-model.md](object-model.md); feature matrix: [feature-coverage.md](feature-coverage.md).

## Adoption approach

Assess organization size and operational needs separately.
An individual can adopt feedback, release, incident, and maintenance modules as soon as a product goes live; allocate responsibilities and adjust collaboration policy when colleagues join.
This is a handbook design recommendation that follows the research scope’s future extension boundaries.

1. Apply the core rules to every work item, establishing deliverables, responsibility, and acceptance evidence.
2. Select collaboration or operations capabilities from the trigger table.
3. Use environment policy to map actual Teams, statuses, permissions, tools, and responsible people.
4. Validate configuration and handoff with one representative work item before broader adoption.

“Recommendation” below describes workflow design; “documented fact” is limited to product behavior explicitly stated in the sources.
User policy for this project follows [AGENTS.md](../AGENTS.md), including outcome-based acceptance, current conclusions in issue bodies, new information in comments, and records of actual work only.

## Four responsibility categories

These proposed module boundaries inform later skill architecture decisions.

| Category | Responsibilities | Inputs and outputs | Maintenance responsibility |
| --- | --- | --- | --- |
| Core rules | Outcomes and completion criteria, decomposition, dependency assessment, current conclusions, evidence, and handoff | Requirements and current issues in; verifiable work, result links, and current state out | Handbook maintainers own shared principles; work owners maintain the facts of their work |
| Roles | Decide who prioritizes requirements, executes, reviews, accepts, releases, and responds to incidents | Required responsibilities in; named owners and handoff recipients out | Product or project owner assigns responsibilities; update at handoff |
| Workspace policy | Map shared concepts to actual Workspace/Team, statuses, labels, templates, permissions, scheduling, and integrations | Environment inventory in; actual IDs/names, scope, change permissions, and capability verification records out | Designated configuration maintainer; actual changes remain subject to platform permissions |
| Operations modules | Specialized inputs, decisions, and outputs for customer feedback, releases, incidents, reliability, and periodic maintenance | Events, feedback, or schedules in; ordinary issues, operations records, improvements, and notification requests out | Each enabled module has a named maintainer; one person may hold multiple roles |

The core uses meanings such as “ready,” “in progress,” and “completed”; policy maps these to environment status IDs and completion criteria.
Roles use responsibility names; person IDs, Team IDs, and actual permissions belong in environment policy.
Operations modules reuse core acceptance and dependency rules; load module-specific data only for the relevant context.

For example, the release module requires a target environment and deployment evidence; policy then chooses native Releases or a release record within an issue.
These categories allocate content responsibilities without predetermining one SKILL.md, multiple skills, or a repository tree; [Skill architecture](../design/skill-architecture.md) determines packaging.

## Roles and handoff

These are recommendations for work responsibilities; one person may hold several roles.
“Product owner,” “reviewer,” and “release owner” are workflow roles, not native Linear permission types.

| Responsibility | Individual + Agents | Small team | Required handoff information |
| --- | --- | --- | --- |
| Requirements and priorities | The individual decides goals, scope, and acceptance criteria | Designated product or project owner | Adopted decisions, tradeoff rationale, completion criteria |
| Issue accountability and execution | The individual owns the outcome; Agents execute authorized work | One Assignee per item; execution may be delegated to an Agent | Execution scope, current conclusions, results, blockers |
| Review and acceptance | The author supplies self-check evidence; arrange another person when independent review is needed | Policy names the reviewer and the person accepting the result | Verification method, results, remaining problems, review conclusions |
| Configuration maintenance | The individual maintains environment mappings | Designated maintainer with confirmed administrative permissions | Effective scope, before/after configuration differences, affected work |
| Releases and operations | The individual owns releases, feedback, and incident handling | Name owners for each release and incident, with backups | Environment, incident impact, recovery evidence, follow-up work, messages to send |

Documented fact: an issue has one Assignee at a time. Native delegation lets a human retain responsibility, and an Agent needs access to the Team. [Assign and delegate issues](https://linear.app/docs/assigning-issues#delegating-to-agents)
An external MCP session therefore needs locatable execution records. Whether it maps to a native Agent identity must be established from tool capabilities; using an Agent does not establish that delegation is configured.

Documented fact: all Free plan members are Admins. Team owner and Guest roles require Business/Enterprise, and Team owners can restrict administration of some settings. [Members and roles](https://linear.app/docs/members-roles#role-types)
Workflow review responsibility cannot replace platform access control, and upgrading a plan does not allocate responsibilities.

## Extension triggers and settings

The following recommendations use actual needs as triggers, with no headcount or issue-count threshold.

| Trigger | Configuration or policy change | Adoption verification |
| --- | --- | --- |
| Another member begins sharing delivery | Name Assignees, reviewers, and decision owners; add handoff entry points and notification responsibility | The recipient can read the results and determine the next action |
| Work regularly needs a shared fixed time window | Define scheduling cadence and capacity review; enable Team Cycles when needed | Pilot one window and record unfinished work’s next steps separately from release plans; Cycles are not tied to Releases. [Cycles](https://linear.app/docs/use-cycles) |
| A work area needs a different workflow, schedule, or access boundary | Evaluate another Team; map statuses, labels, templates, members, Agent access, and integrations | Compare target settings, relationships, and member visibility with a representative issue before adjusting work in batches |
| Cross-domain work needs a shared result and ongoing coordination | Maintain one Project brief and add participating Teams; give each issue its primary home | Each issue has one Team and at most one Project; shared results have references and acceptance by each party. [Teams](https://linear.app/docs/teams#tips-on-structuring-teams), [Projects](https://linear.app/docs/projects#add-issues-to-a-project) |
| Customer feedback or integrations continually introduce requests | Enable feedback handling; define intake owner, duplicate-search entry point, and response deadlines; configure Triage and Customer Requests as needed | A representative source reaches the intake queue with source, decision, and owner preserved; check templates because they may override default Triage status. [Triage](https://linear.app/docs/triage#create-issues) |
| Users begin depending on production | Enable release and incident modules; add environments, release owners, recovery entry points, and notification policy | One release can be traced to deployment and verification evidence; one incident exercise identifies the responder and follow-up improvements |
| Backup recovery, dependency updates, or reliability checks develop a regular cadence | Enable maintenance; set cadence, Team time zone, completion criteria, and maintainer | Check unfinished previous work and the new period’s work; native recurrence is time-triggered, and template updates do not propagate to existing recurrences. [Create issues](https://linear.app/docs/creating-issues#create-recurring-issues) |
| External collaborators need only part of the work information | Confirm Guest/Team access, shareable results, and integration visibility; name an internal contact | Use the actual collaborator role to verify issue, attachment, and source access; Customer Requests cannot be the sole entry point for Guests. [Members and roles](https://linear.app/docs/members-roles#guest), [Customer Requests](https://linear.app/docs/customer-requests#faq) |
| Formal audit, organization-wide access, or compliance requirements arise | Record requirements and open questions under enterprise governance; create separately verifiable research | Identify the requirement owner and decision basis; see the enterprise governance table |

Teams can configure workflows independently; Projects can span Teams, while an Issue belongs to one Team. [Teams](https://linear.app/docs/teams#tips-on-structuring-teams)
Check plan allowances before adding a Team. Adding an Agent or launching a product does not by itself justify another Team.
This follows the [feature selection table in object-model.md](object-model.md#feature-selection-table).

## Operations modules

These are recommendations for minimum workflow interfaces.
Enable them according to actual product needs; an individual may start with one module.

| Module | Inputs and responsibility | Minimum outputs and completion judgment | Optional features and boundaries |
| --- | --- | --- | --- |
| Customer feedback | Source, problem, impact; intake owner handles duplicates, missing information, and priority | Locatable source, adopt/reject/request-information decision, corresponding issue; replies have a recipient and authorization | Customer Requests can link to issues/projects and requires an Admin to enable; core functionality spans Free/Basic/Business/Enterprise, with separate plan restrictions for integrations. [Customer Requests](https://linear.app/docs/customer-requests#configure) |
| Releases | Verified changes, target environment, version, release owner | Deployment record, environment verification, recovery method, release notes; evidence determines whether users received the change | Native Releases requires Business/Enterprise; CI setup uses a pipeline access key. An issue can initially record external CI/CD evidence. [Releases](https://linear.app/docs/releases#ci-setup) |
| Incident | Alert or report, affected service, start time; named responder | Impact and response timeline, recovery evidence, cause or open questions, follow-up work with owners and acceptance criteria | Linear tracks work; designated operations tools and runbooks handle detection, immediate alerts, and recovery. Triage responsibility can connect to on-call sources but requires separate setup. [Triage](https://linear.app/docs/triage#triage-responsibility) |
| Reliability and maintenance | Scheduled checks or incident improvements; named maintainer and check scope | Results per period, anomaly handling, improvement issues, next check; service goals include metric source, interval, and thresholds | Recurring issues are optional; define the check method and use of results before deciding on automation. [Create issues](https://linear.app/docs/creating-issues#create-recurring-issues) |

One person can perform the minimum product release path: organize feedback → accept changes → release and record production evidence → track problems and maintenance.
Even when one person holds all roles, each record must distinguish implementation results, deployment results, and acceptance conclusions.
Whether a merged PR or Done status triggers completion depends on issue completion criteria and environment policy; official Releases documentation also distinguishes Done from actual delivery to users. [Releases](https://linear.app/docs/releases#overview)

Before disabling an operations module, assign its unfinished work and update event entry points and schedules.
Preserve existing decisions, evidence, and result links so feedback does not continue arriving at an unattended entry point.

## Workspace policy interface

These fields are design recommendations; later architecture determines their exact format.
Policy must support “unconfirmed.” When a required capability is unconfirmed, use the corresponding manual workflow or confirm it first.

| Policy area | Information to record |
| --- | --- |
| Environment mapping | Actual Workspace/Team names and IDs; applicable products, repos, and scope |
| Role mapping | Issue owners, decision-makers, reviewers, release and operations owners; handoff and backup arrangements |
| Workflow | Status meanings and IDs, completion criteria, effects of parent/sub-issue, Git, and release automations |
| Classification and intake | Adopted labels, templates, feedback entry points, intake rules |
| Cadence | Cycles, maintenance cadence, Team time zone, checks for stalled work and missing information |
| Access and capabilities | Plan, roles, Team access, available native UI/API/MCP operations, verification dates and evidence |
| Operations configuration | Enabled modules, release environments, deployment/monitoring/runbook entry points, notification recipients and authorized scope |
| Maintenance | Policy owner, effective version, sources, affected workflows; verification entry points after configuration changes |

Read the actual environment before resolving names or IDs.
Map existing names directly where possible; do not encode example statuses or a personal Workspace ID as shared rules.
When capabilities are unclear, confirm settings through the [environment inventory](../skills/linear-handbook/references/workspace-setup.md), then check available operations against the [tool capability research](agent-tool-capabilities.md).

## Migration example: two collaborators join an individual’s live product

This is a design example, assessed by comparing responsibilities, object constraints, and result entry points step by step.
Policy values are assumptions defined for the example.

### Starting point and goal

- Starting point: one developer with multiple Agents manages a product’s frontend and API repos in one Team.
- Change: the product gains production users; a developer and a support collaborator later join.
- Goal: every feedback item has an intake owner, each release can be traced to production evidence, and another person can take over any work item.
- Assumption: all three collaborators have the required access to the same Team and share a workflow; no additional Team or paid operations feature is required.

### Migration steps

1. The individual first adds feedback entry points, release environments, deployment/monitoring/runbook links, and owners.
   Record feedback sources, release evidence, and incident follow-up manually in ordinary issues to make operations usable.
2. Use “Subscriptions work in production” as a representative outcome.
   Frontend and API issues in the existing Project provide feature verification. Separate release work records the version, production verification, and recovery entry point; the Project brief links the results.
3. When colleagues join, explicitly assign each issue’s Assignee, current reviewer, and release owner.
   The support collaborator checks duplicates and handles initial intake; the product owner makes tradeoffs. Record Agent execution scope and handoff evidence in the work item.
4. Run the intake process with feedback that “the subscription button does not work.”
   Record the source and impact, link existing fix work, and confirm the recipient can read the results. Add production verification after the fix, then reply within authorized scope.
5. Keep the existing Team because all three share a workflow.
   Evaluate Cycles when fixed scheduling becomes necessary; inventory Triage and Customer Requests when feedback volume rises; evaluate Releases when release-environment views are needed.
6. Evaluate a separate Team if support later needs independent statuses or access boundaries.
   List current mappings and affected objects, then verify target statuses, relationships, visibility, and integrations with one representative issue before adjusting other work.
   If the pilot fails, stop expanding, repair from saved configuration and work mappings, and confirm someone still owns the original workflow.

### Walkthrough acceptance

- [x] All four operations modules are available at the individual stage; step 1 provides entry points and owners without a headcount threshold.
- [x] Responsibilities for three-person collaboration are explicit; Assignee and Agent execution responsibilities follow “Assign and delegate issues.”
- [x] Frontend and API issues each have one Team and at most one Project, following the object constraints in “Teams” and “Projects.”
- [x] Steps 2 and 4 use production evidence to assess release outcomes; neither Cycles nor Done substitutes for deployment evidence.
- [x] Paid features have pre-adoption checks; a new Team is triggered by different workflow or access needs.
- [x] Pilot scope, expansion criteria, and failure handling are defined; a recipient can trace current results.

## Enterprise governance

This section only defines future research scope and open questions.

| Scope | Open questions |
| --- | --- |
| Multi-Team/multi-Workspace governance | Who decides organization boundaries, shared results, data ownership, and cross-environment integration? How are duplicate sources avoided? |
| Identity and access | Are centralized identity management, offboarding, least privilege, and periodic access reviews required? What data does each feature and integration expose? |
| Audit and retention | Which operations and decisions must be retained, for how long, who can read them, and how is completeness verified? |
| Change approval and separation of duties | Which operations need independent review or approval? Which roles cannot be combined? How are emergency changes reviewed afterward? |
| Compliance and data handling | What obligations, sensitive-data categories, storage locations, and external processor requirements apply? Who makes that determination? |

## Pre-adoption questions

| Question | Impact and verification method |
| --- | --- |
| Target Workspace plan, roles, and settings | Determine availability of additional Teams, Guests, advanced Triage, and Releases; inventory actual plans and settings before choosing native features |
| External Agent identity and operations | Native delegation requires Team access; compare the current connector and actual account, then read back fields from representative work |
| Release integration trigger | The continuous example in “Releases” can create a completed release on push to main. If deployment runs later, that event is insufficient evidence of production delivery. Include successful production deployment and verification evidence in the actual workflow |
| Guest feedback handoff and integration visibility | The “Customer Requests” FAQ explicitly says Guests cannot see Customer Requests, consistent with “Members and roles”; provide permitted issues and result links for Guests and verify external integration permissions |
| Previous recurring issue remains unfinished | “Create issues” supports time-triggered creation, which does not guarantee non-overlap; check due-time and unfinished-work behavior for a representative recurrence before defining carryover handling |
| Actual data mapping after splitting Teams or roles | Documented facts do not cover this Workspace’s custom settings; verify statuses, labels, templates, relationships, visibility, and integrations with a sample before expanding |

These are configuration-time checks; this deliverable is research and design, with feature evidence based on reading official documentation.

## Source records

All nine sources below are published by Linear and were verified on 2026-09-12.
Page-level publication/update dates were not confirmed; evidence status is “documented.”
Section names support in-page searching; feature restrictions and pre-adoption checks are listed separately above.

| Title and URL | Sections / supported conclusions | Limitations |
| --- | --- | --- |
| [Teams](https://linear.app/docs/teams) | Overview, Team settings, Team limits, Tips on structuring teams; Team selection and scope | Confirm Team allowances and change permissions against the actual plan and policy |
| [Members and roles](https://linear.app/docs/members-roles) | Role types, Admin, Team owner, Guest; roles, permissions, Guest access | Workflow responsibility is not a platform role; verify external integrations individually |
| [Assign and delegate issues](https://linear.app/docs/assigning-issues) | Overview, Delegating to agents; one Assignee and Agent access | Investigate external MCP session identity mapping separately |
| [Triage](https://linear.app/docs/triage) | Configure, Create issues, Automation, Triage responsibility | Three advanced features require Business/Enterprise; templates can override status |
| [Customer Requests](https://linear.app/docs/customer-requests) | Configure, Add requests to issues or projects, FAQ | Core and integration plans differ; FAQ explicitly excludes Guest visibility |
| [Releases](https://linear.app/docs/releases) | Overview, Status automations, CI setup, Example for continuous deployments | Business/Enterprise; compare completion events with the actual deployment workflow |
| [Create issues](https://linear.app/docs/creating-issues) | Create recurring issues | Time-triggered; original templates and existing recurrences are maintained separately |
| [Cycles](https://linear.app/docs/use-cycles) | Page introduction, Configure | Enabled by Team; scheduling and releases are separate |
| [Projects](https://linear.app/docs/projects) | Overview, Add issues to a project | Cross-Team projects; each issue belongs to one Project |

## Handoff

1. The four responsibility categories and policy interface inform packaging and on-demand loading decisions in [Skill architecture](../design/skill-architecture.md).
2. Minimum outputs for feedback, releases, incidents, and maintenance inform authoritative storage locations for runbooks, postmortems, and other artifacts in the [documentation guide](../skills/linear-handbook/references/documentation.md), then the [maintenance checklist](../skills/linear-handbook/references/maintenance.md) expands the corresponding checks.
3. The migration example informs initialization and handoffs across roles; actual configuration starts with an environment inventory and representative-work verification.

- [x] Extension triggers and settings cover collaboration, operations, and governance.
- [x] Roles, platform permissions, environment policy, and operations-module responsibilities are separated.
- [x] The individual adoption path, enterprise governance questions, and migration example are complete.
- [x] Official feature facts have sources and verification dates; recommendations and user policy are identifiable.
- [x] The migration example checks responsibilities, object constraints, and result entry points individually.
