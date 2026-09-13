# First-version feedback and adopted decisions

Review date: 2026-09-13.

This record maps received user feedback and decisions adopted for this version to the currently effective documents.
Original conversation references follow [scope-and-sources.md, Confirmed baseline](../research/scope-and-sources.md#confirmed-baseline).

## D01 Audience and environment policy

- Source: user request to focus the first version on individual developers with multiple Agents.
- Decision: adopted.
- Impact: separate shared rules from replaceable environment policy.
- Effective location: [policy.md](../skills/linear-handbook/references/policy.md).
- Check: the entry point loads policy according to operational needs; adopters supply actual environment values.

## D02 Line breaks and lists

- Source: [AGENTS.md, Required writing format](../AGENTS.md#required-writing-format).
- Decision: adopted.
- Impact
  - Each item expresses one independently understandable piece of information.
  - Details within a topic retain a second list level.
  - Completed items use numbering.
  - Acceptance results use checkboxes.
  - Steps within one acceptance item use nested numbering.
- Effective location: [writing.md, Format](../skills/linear-handbook/references/writing.md#formatting).
- Scenario check: [Core scenarios](core-scenarios.md) preserve list rework and revisions to filter-set semantics.
  - Independently failing outcomes appear as separate items.
  - Date and category conditions jointly determining one result preserve intersection semantics.

## D03 Concepts and issue entry points

- Source: user requests for native issue mentions and conceptual writing.
- Decision: adopted.
- Impact
  - General rules use role and object concepts.
  - Specific related work in Linear bodies uses native mentions.
- Effective location: [writing.md, Evidence and deliverable entry points](../skills/linear-handbook/references/writing.md#evidence-and-output-links).
- Check: attachment entry points use stable issue URLs and filenames.

## D04 Remove unnecessary content first

- Source: [AGENTS.md, Content selection and work records](../AGENTS.md#content-selection-and-work-records).
- Decision: adopted.
- Impact
  - Determine reader purpose before choosing wording and structure.
  - Work records describe only actions actually performed.
  - Preserve specific differences only when they affect assessment of the result or the next step.
- Effective location: [writing.md, Content selection](../skills/linear-handbook/references/writing.md#content-selection).
- Final adjustment: replaced the old body's requirement for routine statements of unperformed work with deliverables, feedback references, and actual verification.

## D05 Keep current conclusions in the body

- Source: [AGENTS.md, Maintain issue bodies](../AGENTS.md#maintain-issue-bodies).
- Decision: adopted.
- Impact
  - Update the body with goals, the effective approach, and deliverable entry points.
  - Comments preserve new findings and decision reasons.
- Effective location: [writing.md, Issue body and comments](../skills/linear-handbook/references/writing.md#issue-body-and-comments).
- Check: [Recovery scenarios, Concurrent human rewrite](recovery-scenarios.md#concurrent-human-rewrite) preserves and reads back the user's complete JSON version.

## D06 Assemble from delivered content

- Source: [content-migration.md, Authoritative sources](../design/content-migration.md#authoritative-sources).
- Decision: adopted.
- Impact
  - `skills/linear-handbook/` maintains effective workflows and templates.
  - Maintain research evidence and operational documents separately according to current content ownership.
  - Map each of the twelve research areas to an entry point within the package.

## D07 Impeccable structural reference

- Source: the user supplied `pbakaus/impeccable`.
- Decision: adopted its structural principles.
- Impact
  - Maintain one source directory.
  - Load references by task.
  - Add build transformations when provider format or path differences are confirmed.
- Verification and pinned commit: [skill-architecture.md, Additional decision: Impeccable structure](../design/skill-architecture.md#additional-decision-impeccable-structure).

## D08 Completion criteria and publication

- Source: first-version integration acceptance and publication requirements.
- Decision: adopted.
- Impact: complete acceptance against this version's deliverables and received corrections.
- Required inputs for public publication: the target GitHub repository and publication authorization.
- Operational entry point: [Maintenance guide](../docs/maintenance.md).
