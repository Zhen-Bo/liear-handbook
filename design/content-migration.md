# Content reuse and source maintenance

Compiled: 2026-09-13.

## Authoritative sources

- `skills/linear-handbook/`: the sole maintained source for operating workflows, examples, and templates.
- `research/`: research questions, sources, findings, and adoption rationale.
- `design/`: architectural choices and content mappings.
- `validation/`: check programs, fixed cases, and de-identified evidence.
- Linear: unresolved proposals, work decomposition, and execution discussions.

## Reuse rules

1. Preserve sources and verification dates for feature research before updating adopted conclusions in the skill.
2. Record the reasons for design changes and affected entry points.
3. Maintain operating documents directly in `references/` and templates in `assets/templates/`.
4. Validate fixed inputs, expectations, and results, preserving the tested version.
5. Keep private operating logs and generated temporary files in excluded directories.

## Mapping the twelve scope areas

| Research area | Authoritative entry point | Coverage and follow-up deliverables |
| --- | --- | --- |
| Concepts and feature selection | [object-model](../skills/linear-handbook/references/object-model.md) | Eight objects, product/repo mapping, selection examples |
| Environment initialization | [workspace-setup](../skills/linear-handbook/references/workspace-setup.md) | New and existing environments, minimum setup, roles and capabilities |
| Project creation | [project-planning](../skills/linear-handbook/references/project-planning.md) | Brief, initial work, milestones, genuine dependencies |
| Issue classification | [issue-types](../skills/linear-handbook/references/issue-types.md) | Thirteen types and five type templates |
| Issue decomposition | [issue-decomposition](../skills/linear-handbook/references/issue-decomposition.md) | Session outcomes, scope changes, three examples, parent integration |
| Writing | [writing](../skills/linear-handbook/references/writing.md) | Bodies, comments, Project updates, hierarchical formatting |
| Lifecycle | [issue-lifecycle](../skills/linear-handbook/references/issue-lifecycle.md) | Execution, blocking, acceptance, completion, cancellation, reopening, duplicates |
| Document management | [documentation](../skills/linear-handbook/references/documentation.md) | Authoritative full text, access, ownership, versions, staleness |
| Other features | [feature-coverage](../skills/linear-handbook/references/feature-coverage.md) | Nine feature categories and conditional adoption; maintenance supplies operational checks |
| Agent operations | [multi-agent-coordination](../skills/linear-handbook/references/multi-agent-coordination.md) | Supported by three references on tool capabilities, recovery, and authorization boundaries |
| Skill repository | [SKILL.md](../skills/linear-handbook/SKILL.md) | Single directory and complete routing |
| Scenario validation | [Validation entry point](../validation/README.md) | Assembly structure, core scenarios, recovery scenarios |

## Legacy directory consolidation

- `handbook/` and `examples/` were consolidated into the skill’s `references/`.
- `templates/` was consolidated into the skill’s `assets/templates/`.
- Document tool capabilities are recorded in [Agent tool capabilities — Documents](../research/agent-tool-capabilities.md#documents).
- Manual checks of the original documents are preserved in [pre-assembly document checks](../validation/document-checks.md).
- Historical file hashes identify the delivery at that time; they do not require current sources to remain unchanged.
