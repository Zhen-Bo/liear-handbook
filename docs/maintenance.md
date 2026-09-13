# Maintenance guide

## Update content

`skills/linear-handbook/` is the source for workflows and templates and the complete installation unit.

1. Update the relevant reference or template.
2. Support feature facts with official document titles, section names, and verification dates.
3. When adding a document, add an entry point in SKILL.md.
4. Check relative links and affected usage scenarios.

Shared writing requirements live in [writing.md](../skills/linear-handbook/references/writing.md).
See [AGENTS.md](../AGENTS.md) for repository maintenance rules.

## Verification

- [ ] Links from the skill entry point and supporting documents resolve.
- [ ] The complete skill can be read from an isolated directory.
- [ ] Updated scenarios preserve the original requirements and acceptance criteria.
- [ ] Completed templates clearly express the problem and delivery conditions.
- [ ] Public files do not depend on private issues or local machine paths.

Record the version used and actual verification results.
Rerun affected scenarios after changing templates or workflows; link checks do not replace behavior validation.

## Update an installation

1. Save personal changes in the currently installed copy.
2. Copy the complete new version into a separate directory.
3. Compare the versions and merge the changes you need to keep.
4. Check the entry point and supporting files before replacing the installed copy.

Keep Workspace settings in the user's environment policy so skill updates do not overwrite them.

## Where content belongs

- `skills/linear-handbook/`: installable guides, examples, and templates.
- `research/`: complete research evidence and source excerpts.
- `design/`: architecture decisions and content maintenance mapping.
- `validation/`: check scripts, fixed cases, and de-identified validation records.
- Linear: proposals, tasks, and working discussions; incorporate adopted conclusions into the repository.

Store private logs in `validation/private/`.
Store newly generated check output in `validation/generated/`.
Store delivery ZIP files in `deliverables/`.
Git excludes these three locations and `.tmp/`.

Fixed synthetic test data may be versioned, retaining evidence of failures and corrections.
Historical reports identify the tested version; rerun affected scenarios after changing the skill.
See the [validation guide](../validation/README.md) for commands.
