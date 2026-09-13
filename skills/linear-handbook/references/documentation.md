# Documentation placement and maintenance guide

- Context: An individual developer working with multiple Agents.
- Verified on: 2026-09-13.

This guide's placement choices and maintenance workflows are first-edition recommendations.
See "Linear features and sources" for platform feature evidence.
[Writing rules](writing.md) govern this edition's writing and issue body maintenance policy.

- Object selection basis: [object-model.md](object-model.md).
- Periodic check entry point: [maintenance.md](maintenance.md).

## Placement decisions

1. Identify the reader need served by the document.
   - Understand the goal.
   - Assess the result.
   - Take a specific action.
2. Maintain short content directly in an issue or project description when it can be explained there.
3. When a separate full document is needed, choose its location by purpose.
   - Use the repo for content that needs review alongside code versions.
   - Use a Linear document for long collaborative content evolving with Linear work.
   - Use an external document when an existing knowledge base or specialized layout is needed.
4. Confirm that intended readers and executing Agents can access the location.
5. Designate one authoritative full text; retain purpose and links elsewhere.
6. When acceptance evidence must be preserved, save a separate snapshot labeled with its source version.

### Seven document categories

Adjust the paths below to the existing project structure.

- Brief
  - Put the short version in the project description by default.
  - Use a project document when a separate long text is needed.
  - Use an external document when departments already share an editing space.
  - Use repo `docs/brief.md` when it must be versioned.
  - Keep the goal and authoritative full-text link in the Project.
  - Suggested maintainer: Project lead.
- PRD
  - Use a project document by default.
  - Use repo `docs/product/` when requirements need review with code.
  - Continue using the existing document platform for external product collaboration.
  - Keep a summary of adopted requirements in the Project.
  - Link implementation issues to the corresponding sections.
  - Suggested maintainer: Requirements decision-maker.
- Research
  - Use repo `research/` by default.
  - Evidence record
    - Sources.
    - Verification date.
    - Distinction between facts and inferences.
  - Use an issue document or project document for short-term joint exploration.
  - Continue using the existing analysis platform for external sharing.
  - Summarize current conclusions and their impact in the research issue.
  - Suggested maintainer: Research owner, with a successor designated after closure.
- ADR
  - Use repo `docs/adr/` by default and state the applicable code version.
  - Use a shared documentation repo for decisions spanning repositories.
  - Use a Linear document or existing decision repository when there is no code-version relationship.
  - Link the decision issue to the ADR.
  - Link superseded decisions to the new ADR.
  - Suggested maintainer: System maintainer.
- Runbook
  - Put deployment- or command-dependent content in the service repo's `docs/runbooks/`.
  - Put common manual workflows in a team document.
  - Use an existing operations knowledge base when independent access during incidents is needed.
  - Link the service entry point to the applicable version.
  - Update affected steps when the system changes.
  - Suggested maintainer: Service maintainer.
- Postmortem
  - Keep the recovery summary in the incident issue.
  - Put necessary long text in an issue document.
  - Use repo `docs/postmortems/` or an existing incident repository for analysis across incidents.
  - Related entry points in the incident issue
    - Timeline.
    - Cause evidence.
    - Improvement issues.
  - The incident coordinator should complete it, then hand it to the service maintainer.
- Code documentation
  - Use the repo by default, placing content in the README or near the code as appropriate.
  - Publish from the repo when public readers need a documentation website.
  - A site generated from the repo treats the repo as its authoritative source.
  - Keep specialized external references at their original sources.
  - Link the issue to the delivered version.
  - Suggested maintainer: Code module maintainer.

### Suggested Linear document ownership

- Project: Specifications and shared context for that outcome.
- Initiative: Shared goal context across projects.
- Team: Common workflows across projects.
- Issue: Supplementary long text for one work item.
- Cycle: Records for that period.
  - Give long-term runbooks a separate, continuously maintained entry point.

Before creating a new project, check whether existing ownership meets the documentation need.

## Authoritative version and links

- Maintain effective information in the issue body according to [writing](writing.md).
  - Goal.
  - Adopted conclusions.
  - Delivered outputs.
  - Open questions.
- Link full documents to the authoritative full text.
- Comments preserve findings and reasons that add information.
- Link everyday operations to the currently effective version.
- Link code evidence to a fixed commit.
- State the tested version in acceptance evidence.
- State the applicable baseline in ADRs.
- Relative paths can be used within the repo.
- Provide an accessible remote entry point when entering from Linear.
- Use a stable issue page and attachment name as the entry point for attachment snapshots.
  - Obtain a fresh valid URL when downloading.
  - State the snapshot's relationship to the authoritative full text.
- Use native issue mentions for related issues and explain the relationship.

When copies conflict:

1. Identify the source from the authority statement.
2. Compare applicable versions.
3. Merge new, effective content into the authoritative full text.
4. Update other entry points.

The last-modified time is only an investigative clue.
Verify link readability as the intended reader; one Agent reading successfully proves only that its connection works.

## Maintenance responsibility and information

Documents in continuing use need identifiable maintenance responsibility.
In an individual project, the developer assumes this responsibility by default; Agents may perform authorized revisions.
Do not infer maintenance responsibility from creator or last-editor fields.

Record the following in the document or existing directory as needed for ongoing maintenance.
Reference existing entry points directly when they already identify the information.

- Purpose.
- Scope.
- Applicable version.
- Named maintainer.
- Authoritative entry point.
- Latest verification date.
- Verified version: Include when a fixed execution baseline is required.
- Known gaps: Include when parts are no longer valid.
  - Affected operations.
  - Alternative entry point or verification work.
  - Responsible owner.

Transfer steps:

1. The successor confirms read access.
2. The successor confirms edit access.
3. The successor confirms the applicable baseline.
4. Update the maintainer.
5. Update affected entry points.

When there is no successor, the project lead or service maintainer should designate one.
Until validity is restored, identify affected operations and pending work.

## Updates and invalidation

Start with a monthly check and adjust according to impact.
When an event occurs, check affected content first.
See "Recurring work and document validity" in maintenance.md for the periodic workflow.

- Requirements or adopted decisions change
  - Update the Brief or PRD.
  - Update current conclusions in the issue.
  - Retain necessary links to decision reasons.
  - Assign decision responsibility for unresolved items.
- Code or execution environment changes
  - Compare code documentation.
  - Compare the runbook.
  - Reverify affected steps and record the version.
  - When verification is missing, identify unreliable steps and the work to check them.
- Incident recovery or cause evidence changes
  - Update postmortem facts.
  - Identify inferences still needing confirmation.
  - Update the timeline.
  - Link follow-up improvement work.
  - Revise the runbook when necessary.
- Platform capabilities or sources change
  - Reread sources supporting the conclusion.
  - Update the verification date.
  - Correct affected operations.
  - Assign verification responsibility for unconfirmed conditions.
- Links break or permissions change
  - Locate the same authoritative content.
  - Update reference entry points.
  - Confirm access for intended readers.
  - If content cannot be found, record the gap and owner.
  - Set the next verification event or date.
- Decisions are superseded or the purpose disappears
  - Keep reasons and replacement links in old ADRs.
  - Mark historical snapshots as superseded.
  - Mark invalid operational documentation as no longer applicable at its entry point.
  - Remove purposeless duplicate full texts within the authorized scope.

Document validity depends on whether content still fits its current purpose and evidence.
Only the affected sections may need to be marked.

### Updates by multiple Agents

1. Confirm the change scope and maintenance responsibility.
2. Read the latest document and related issues.
3. Read the target again before writing and merge effective content added in the meantime.
4. Prefer precise local edits.
5. If a safe merge is impossible, save the draft and conflict locations for the maintainer to decide.
6. Read back the revision, then add the output links.
7. When the operation's outcome is unclear, read back first before deciding whether to retry.

- [ ] The revised document is usable by the next reader.
  1. Read back the content.
  2. Check list hierarchy.
  3. Open output links.
  4. Confirm the authority statement.
  5. Confirm ownership and reader permissions.

## Linear features and sources

Verified on: 2026-09-13.
The feature facts below come from official documentation review.

- [D01 Documents](https://linear.app/docs/documents)
  - Page introduction: Document ownership
    - Project.
    - Initiative.
    - Team.
    - Issue.
    - Cycle.
  - Edit documents: Collaborative editing is supported.
  - Version history: Earlier document versions can be viewed and restored.
  - Version history: Project descriptions also have version history.
  - Reference documents: Use `@` in the editor to select a document.
  - Link to headers: Section links can be copied.
- [D02 Project overview](https://linear.app/docs/project-overview)
  - External links: External links can be added to Resources.
  - Project documents: Documents can be created in Resources.
- [D03 Team pages](https://linear.app/docs/default-team-pages#team-documents)
  - Team documents: Team documents can contain shared content across projects.
  - Team documents: Official documentation lists runbooks as a use case.
- [D04 Exporting Data](https://linear.app/docs/exporting-data)
  - Issue view CSV exports: CSV does not include attachment files.
  - Copy issues as markdown for LLMs: Issues can be copied as Markdown.
  - Copy issues as markdown for LLMs: Documents can be copied as Markdown.

### Confirm tool capabilities

- Check the current schema for available document parents and disambiguation fields.
- Verify whether creation, editing, reparenting, and version restoration each have an available interface.
- When the tool lacks restoration, use an authorized native interface and preserve subsequent changes first.
- Obtain a valid URL again when an attachment URL expires.

### Before operating

- Retain delivered IDs and URLs when locating documents.
- Handle pagination when listing and define scope using actual tool fields.
- Preserve original files when saving snapshots.
- Verify each required item after export.
  - Text.
  - Images.
  - Attachments.
  - Relationships.

Confirm the following in the actual environment:

- Whether the target feature applies to the plan in use.
- Whether intended readers have access.
- Whether the executor has edit permission.
- Whether version history covers the required period.
  - Arrange snapshots when long-term retention is needed.
