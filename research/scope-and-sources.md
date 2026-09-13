# Research scope, source index, and feedback rules

## Goal and usage

Build a Linear handbook skill for an individual developer with multiple Agents.
Enable Agents to select features, plan and decompose work, update progress, verify acceptance, and hand off work.
This document is the entry point for further research; individual studies supply feature choices and operating conclusions.

The first version uses English while retaining Linear’s original terminology.
Separate shared rules from environment policy so one workspace’s names, statuses, or permissions do not become universal settings.
See [AGENTS.md](../AGENTS.md) for this project’s execution environment and writing format.

In each session:

1. Read the latest AGENTS.md, target issue, parent, prerequisite deliverables, and relevant comments.
2. Confirm this session’s deliverable, acceptance criteria, and received feedback.
3. Find an entry point in the source index and read the specific pages supporting this session’s conclusions.
4. Record conclusions, evidence, and limitations, and complete a result that can be accepted in this session.
5. Update result locations, verification results, open questions, and next steps.

## First-version scope and research questions

These twelve topics define the research scope. The table lists questions and expected deliverables, not a claim that research is complete.

| Topic | Research questions | Expected deliverable |
| --- | --- | --- |
| Concepts and feature selection | How do Workspace, Team, Initiative, Project, Milestone, Cycle, Issue, and Sub-issue relate? How do products map to repositories? | Object relationships and selection decision table |
| Environment initialization | What settings need inventory in new and existing workspaces? How should statuses, labels, templates, permissions, and integrations be configured incrementally? | Minimum setup and takeover checklist |
| Project creation | How should an idea become outcomes, scope, constraints, and success criteria? How are milestones and dependencies created? | Project brief and creation workflow |
| Issue classification | How should bugs, features, improvements, refactoring, research, performance, security, migration, documentation, tests, incidents, and operations be expressed? When is a parent needed? | Work types and template selection table |
| Issue decomposition | How can children have independent outputs, acceptance, and session boundaries? How should shared foundations, integration, blockers, and scope expansion be handled? | Decomposition workflow and before/after examples |
| Writing | What belongs in titles, bodies, comments, and project updates? When should current agreement be updated or history appended? | Templates, comment timing, and good/bad comparisons |
| Lifecycle | How are intake, scheduling, execution, blocking, review, acceptance, closure, and reopening handled? How do merge, deployment, and completion differ? | State transitions and progress update rules |
| Document management | What belongs in Linear or the repository? How are ownership, access, versions, staleness, and duplicate information handled? | Document placement and maintenance guide |
| Other features | When are views, search, Triage, intake, notifications, analytics, bulk operations, and import/export useful? What plan restrictions apply? | Feature coverage matrix |
| Agent operations | How are claiming, duplicate avoidance, parallel coordination, write confirmation, retries, and insufficient permissions handled? How do native features, API, MCP, and current tools differ? | Operating protocol, capability comparison, and recovery workflow |
| Skill repository | How should the core entry point and modules be divided? How are installation, references, versions, and source maintenance handled? | Repo structure, installation, and usage design |
| Scenario validation | How is correct Agent behavior assessed during creation, takeover, ambiguous requests, decomposition, blocking, changes, partial success, and handoff? | Scenarios, expected behavior, and acceptance evidence |

Six parents group the deliverables, with each sub-issue serving as one session’s work unit.
This document establishes scope, source indexing, and feedback rules without prescribing unverified operating answers.

## Future extension boundaries

- Small teams: reserve role allocation, review responsibility, team scheduling, and handoffs between members.
- Live-product operations: reserve customer feedback, releases, incidents, reliability, and maintenance workflows.
- Enterprise governance: record extension boundaries for multiple teams, permissions, auditing, change approval, and compliance.

Treat organization size and product operations needs separately.
An individual developer may also need formal product operations.
The first version reserves extension points; later research delivers concrete migration designs.
Confirm the target repository and publishing authorization before public release.

## Source index

The following entry points were opened and confirmed readable on 2026-09-12.
Verification dates indicate when they were read, not publication dates or verification of every linked page.
For pages without a listed publication date, the page-level publication/update date was not confirmed.

| Publisher / title and URL | Location and research purpose | Verified | Limitations |
| --- | --- | --- | --- |
| Linear: [Linear Docs](https://linear.app/docs) | Homepage categories and Linear basics; locating feature explanations | 2026-09-12 | Entry point; read individual feature pages separately |
| Linear: [Start Guide](https://linear.app/docs/start-guide) | Onboarding workflow; starting point for initialization and projects | 2026-09-12 | Compare existing environment before configuration |
| Linear: [Linear Developers](https://linear.app/developers) | GraphQL API, Authentication, Agents, and SDK categories | 2026-09-12 | Does not establish that the current connector exposes every capability |
| Linear: [The Linear Method](https://linear.app/method) | Direction and Building; planning, decomposition, and writing methods | 2026-09-12 | Methodology informs recommendations, not mandatory platform rules |
| Linear: [Changelog](https://linear.app/changelog) | Update index; tracking feature changes | 2026-09-12 | Formal citations require individual update articles and dates |
| Linear: [Pricing](https://linear.app/pricing) | Plan comparison; locating feature availability | 2026-09-12 | Confirm the actual workspace plan through inventory |
| Linear: [Parent and sub-issues](https://linear.app/docs/parent-and-sub-issues) | Parent/child work; starting point for decomposition research | 2026-09-12 | See object-model.md for modeling constraints and completion behavior |
| Linear: [Agent Interaction Guidelines](https://linear.app/developers/aig) | Agent interaction guidance entry point | 2026-09-12 | Distinguish native Agent integrations from external Agents using MCP |
| Linear: [MCP server](https://linear.app/docs/mcp) | Setup and FAQ; entry point for MCP connection and operations research | 2026-09-12 | Compare client instructions with corresponding official documentation and versions |
| Matt Pocock: [mattpocock/skills](https://github.com/mattpocock/skills) | README, Installation, and skills directory; organization and distribution reference | 2026-09-12 | Third-party skill project; pin a commit and confirm licensing before adopting implementation |

Supported entry-point observations:

- Linear Docs organizes feature and integration documentation; subsequent research should cite specific pages. [Linear Docs](https://linear.app/docs)
- Linear Developers separates API, SDK, and Agent documentation; capability research should preserve these interface distinctions. [Linear Developers](https://linear.app/developers)
- Linear Method provides articles on planning and building practices. [The Linear Method](https://linear.app/method)
- The reference repository emphasizes small, adaptable, composable skills and provides installation instructions; it can inform packaging tradeoffs. [mattpocock/skills](https://github.com/mattpocock/skills)

All observations above were verified on 2026-09-12.
See [object relationships](object-model.md), [feature coverage](feature-coverage.md), and [extension boundaries](extension-model.md) for concrete results; each lists adopted conclusions and open questions.

## Source record format

Each research document cites sources near conclusions and maintains records for the sources it actually uses.
Index entry points do not replace evidence supporting specific conclusions.

```markdown
### Source identification

- Title:
- Publisher/author:
- URL:
- Section/location:
- Publication/update date: write “not provided” if absent, or “unconfirmed” if not checked.
- Verified: YYYY-MM-DD
- Supported conclusion:
- Limitations: plan, permission, platform, version, interface, or context.
- Evidence status: documented / tested / unconfirmed / conflicting.
- Test record: record operations, environment, and results when tested.
```

Formal implementation references to changing repositories should record commits and file locations.
Cite individual update articles rather than only the changelog homepage.
For user requirements or environment observations without public URLs, record a locatable document, issue comment, or conversation passage; do not invent links.

## Evidence classification and conflict handling

| Type | Assessment | Required record |
| --- | --- | --- |
| Feature fact | Behavior explicitly documented by an official source or reproducible environment observation | Source, date, limitations; distinguish documentation confirmation from testing |
| Recommendation | A choice based on methodology, examples, or analysis | Rationale, context, tradeoffs, and aspects still needing verification |
| User policy | An explicit user requirement for this project | Requirement source, scope, effective status, and supersession relationships |

Label inferences as inferences; write unconfirmed content as research questions.
One successful operation supports only that environment and operation, not a guarantee for all accounts or tools.

When conflicts arise:

1. Check whether sources describe the same feature, date, version, plan, permissions, and interface.
2. If feature sources disagree, read specific official documentation and update articles; perform a minimal authorized test if necessary.
3. If unresolved, preserve both sources, the difference, and affected conclusions; mark them unconfirmed rather than prescribing a certain operation.
4. When user policy differs from recommendations, adapt recommendations to the confirmed policy.
5. When platform limits constrain user policy, record the limit and feasible options; ask only if an unresolved choice affects the outcome.
6. When user policies differ, prefer the newer requirement that is more specific to the document, preserving the superseded record.

## Feedback intake and decision records

After receiving a user-provided version or correction:

1. Preserve a locatable source and original intent; identify a full replacement, targeted correction, or proposal still under discussion.
2. Determine affected documents, templates, and rules; do not automatically generalize a specific example into a universal preference.
3. Preserve content and structure for full replacements; update AGENTS.md for new general formatting requirements.
4. Update affected existing results; record where the rule should apply to templates not yet created.
5. Record the reason, verification method, and remaining work.
6. Update the issue body with current conclusions, result links, and verification results; use comments for actual new findings and decisions.

Decision record format:

```markdown
### Decision name

- Received:
- Source: document, comment link, or locatable conversation passage.
- Requirement and rationale:
- Scope:
- Decision:
- Superseded content: record any replaced rules.
- Updated results:
- Verification results:
- Remaining work:
```

### Confirmed baseline

Compiled on 2026-09-12 from project conversations and the current AGENTS.md.
The conversations have no shareable fixed links, so message content identifies sources below; future preferences are not inferred.

| Source location | Decision and rationale | Scope / current handling |
| --- | --- | --- |
| “Focus the first version on an individual developer + multiple Agents” | Complete individual collaboration workflows first and preserve extension boundaries | Adopted in this document |
| Full Project description replacement and three reasons for changes | Break lines by meaning; use bullets for parallel categories; number ordered steps and general conditions | Adopted in AGENTS.md and this document; future templates follow it |
| Full parent issue replacement and acceptance correction | Use checkboxes for acceptance; this overrides numbering for general conditions | Adopted in AGENTS.md and this document |
| “Native issue mention” and “you should be writing the concept” | Use native mentions for related issues in Linear bodies; avoid binding shared rules to specific identifiers | Replaces ordinary Markdown issue links and fixed-identifier examples; recorded in AGENTS.md |
| Example of one verification item with multiple steps | Outer checkbox states the result; inner numbered list states steps | Adopted in AGENTS.md and the acceptance example below |
| AGENTS.md “Help third parties understand quickly” and “Issue body maintenance” | Put delivery goals and current conclusions in the body; comments record actual progress, findings, and decisions | Replaces using comments to record goals and wait for style feedback |
| AGENTS.md “Content selection and work records” | Delete content that does not affect understanding or action before organizing wording and structure; record only actual work | Replaces routine statements about unperformed work and pending review; corrects matching template rules |

Synchronize new corrections into the effective rules; preserve sources and supersession relationships when rationale needs tracing.

## Acceptance and handoff for this item

- [x] The twelve first-version topics and future extension boundaries are listed.
- [x] Source format includes URL, title, verification date, and limitations.
- [x] Feature facts, recommendations, user policy, and conflict handling are defined.
- [x] Entry-point observations have locatable sources and verification dates, with identifiable evidence scope.
- [x] Received formatting corrections have source locations, scope, and current handling records.
- [x] Received corrections on content selection, work records, and issue body maintenance are reflected in rules and templates.

Subsequent research can use this acceptance format:

```markdown
- [ ] Conclusions can be reproduced from sources.
  1. Open each cited page and locate the corresponding section.
  2. Check the conclusion and applicable limitations.
  3. Record the verification date; mark unconfirmed aspects for research.
```

In the next session, select research questions matching the target issue and add specific sources and conclusions.
Each issue body and its attachments maintain result entry points.
Update references and entry points whenever files are renamed or moved.
