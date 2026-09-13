# Linear handbook skill architecture

Decision date: 2026-09-13.
Scope: first version for an individual developer with multiple Agents.

## Adopted structure

Use `skills/linear-handbook/` as a single entry point, loading references and templates by task.
This directory is the complete installation unit and the sole maintained source of distributable content after assembly.

- `SKILL.md` handles triggering, shared decisions, task routing, and policy entry points.
- `references/` holds workflows, feature evidence, examples, and policy contracts to read.
- `assets/templates/` holds deliverable templates to copy and adapt.
- User-designated policy documents or information confirmed in the session supply concrete environment mappings.
- Research evidence is maintained in `research/`.
- Design rationale is maintained in `design/`.
- Validation cases and de-identified evidence are maintained in `validation/`.
- All local references inside the installation package stay within `skills/linear-handbook/`.

This is the project’s design choice.
Its format follows Agent Skills’ “Directory structure” and “Progressive disclosure,” and OpenAI’s “Build skills.” [Agent Skills Specification](https://agentskills.io/specification) [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)

### Options compared

| Option | Suitable context | First-version decision |
| --- | --- | --- |
| One entry point + references | Several steps share objects, policy, and delivery principles and often follow each other within one task | Adopted; initialization, decomposition, updates, and handoff share one policy contract |
| Multiple skills | Each capability has independent triggers, users, and maintenance cadence and can complete work independently | Reevaluate when independent operations capabilities emerge; splitting now would duplicate policy and add dependencies between skills |

One entry point does not mean reading the entire handbook at once.
The entry point explicitly lists loading conditions for each file; presence in the package does not mean a document has been loaded.

## Practices in the reference project

Verified: 2026-09-13.
Pinned version: `mattpocock/skills@3cca18b368ae95cdbdebbff572ccafa662551015`.

- README Installation offers Claude Code plugin and skills.sh installation paths. [mattpocock README](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/README.md#installation-30-second-setup)
  - The plugin supplies a managed collection.
  - skills.sh supplies editable copies of skill files.
- Skill directories are organized into categories such as `engineering` and `productivity`. [plugin.json](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/.claude-plugin/plugin.json#L20)
  - `.claude-plugin/plugin.json` explicitly lists each distributed skill path.
- `tdd/SKILL.md` loads `tests.md` and `mocking.md` with relative links in the same directory. [tdd/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/tdd/SKILL.md#L13)
- The opening of `scripts/link-skills.sh` explicitly identifies it as a maintainer development script, not a supported installer. [link-skills.sh](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/scripts/link-skills.sh#L2)

This version adopts a complete skill directory and conditional references.
Public distribution can add an outer plugin manifest; reading the skill itself does not depend on that manifest.
Current OpenAI documentation recommends plugins for external distribution; this version first validates local installation as a standalone skill. [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)

## File tree

The following is the assembly target; these path names also form the contract for subsequent references.

```text
linear-handbook/
├── AGENTS.md                         Project development instructions
├── research/                         Original research and historical evidence
│   └── sources/                      Original sources and tool declaration snapshots
├── design/
│   ├── skill-architecture.md          This architecture
│   └── content-migration.md           Content ownership and reuse records
├── skills/
│   └── linear-handbook/               Sole installation unit
│       ├── SKILL.md
│       ├── references/
│       │   ├── policy.md
│       │   ├── writing.md
│       │   ├── object-model.md
│       │   ├── feature-coverage.md
│       │   ├── extension-model.md
│       │   ├── agent-tool-capabilities.md
│       │   ├── workspace-setup.md
│       │   ├── project-planning.md
│       │   ├── planning-and-dependencies.md
│       │   ├── issue-types.md
│       │   ├── issue-decomposition.md
│       │   ├── issue-lifecycle.md
│       │   ├── documentation.md
│       │   ├── maintenance.md
│       │   ├── multi-agent-coordination.md
│       │   ├── tool-recovery.md
│       │   ├── agent-boundaries.md
│       │   ├── project-bootstrap.md
│       │   ├── feature-decomposition.md
│       │   └── decomposition-edge-cases.md
│       └── assets/
│           └── templates/
│               ├── project-brief.md
│               ├── bug.md
│               ├── feature.md
│               ├── research.md
│               ├── refactor.md
│               ├── migration.md
│               ├── progress-comment.md
│               ├── project-update.md
│               └── handoff.md
├── validation/                       Scenario and packaging evidence
└── README.md                         Usage, installation, and result entry points
```

- The first version operates through instructions and documents.
- Add `agents/openai.yaml` only when UI metadata is needed.
- Discover execution tools from the environment and verify schemas; do not fix connector names in frontmatter.
- Installation requires neither Node nor Python nor a custom build process.
- Validation tools support maintainer checks and are not user dependencies for running the skill.

## Triggering and loading

`name` is fixed as `linear-handbook`, matching the directory. [Agent Skills Specification](https://agentskills.io/specification)
`description` describes “planning projects, decomposing work, maintaining issues, handing off, and recovering Agent operations in Linear.”
General code implementation and writing unrelated to Linear are outside the trigger scope.
Retain default automatic selection and explicit invocation. [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)

The entry point maintains these shared decisions:

1. Determine the deliverable and current operating scope from the request.
2. When current state is needed, read the target issue, relevant current conclusions, and genuine prerequisite deliverables.
3. Select the matching workflow below and read only required references and templates.
4. Before changing remote objects, confirm existing authorization, actual capability, and target mappings.
5. Verify completion from results, then update authorized targets with current conclusions and result entry points.

`SKILL.md` directly lists these reference paths and loading conditions.
Read extension links within supporting references only when the corresponding problem arises.

| Task | Load first | Conditional extensions |
| --- | --- | --- |
| Select Linear objects or features | `object-model.md` | Read `feature-coverage.md` for plan or feature choices |
| Initialize or take over a Workspace | `workspace-setup.md`, `policy.md` | Read `project-bootstrap.md` when a complete example is needed |
| Plan a Project from an idea | `project-planning.md` | Read `planning-and-dependencies.md` for milestones, dependencies, or capacity; read the matching template when producing a brief |
| Classify or write an issue | `issue-types.md`, `writing.md` | Select one matching type template |
| Decompose large work | `issue-decomposition.md` | Read `planning-and-dependencies.md` to assess blockers; read one of the two decomposition examples only when needed |
| Update, accept, or hand off | `issue-lifecycle.md`, `writing.md` | Read progress-comment, project-update, or handoff templates according to the output |
| Place or maintain documents | `documentation.md` | Read `maintenance.md` for periodic checks |
| Multiple Agents claim work or conflict | `multi-agent-coordination.md` | Read `tool-recovery.md` when an operation’s outcome is unknown |
| Timeouts, rate limits, partial success | `tool-recovery.md` | Read `agent-tool-capabilities.md` and inspect current tools when declarations are unclear |
| Authorization, sensitive information, or external instructions | `agent-boundaries.md` | Read `policy.md` when the target is constrained by the environment |
| Add collaborators or product operations | `extension-model.md`, `policy.md` | Read corresponding parts of `maintenance.md` for enabled workflows |

Except templates, filenames in this table are relative to the package’s `references/`.
There is no requirement to begin every task by reading all research, every policy field, or every example.

## Shared rules and environment policy

Shared rules describe outcomes, responsibility, evidence, and recovery decisions.
`references/policy.md` defines replaceable fields, resolution rules, and handling of unknown values.
`references/writing.md` provides self-contained English writing defaults while retaining Linear’s terminology.

- Writing defaults reuse confirmed formatting and content-selection rules from the current [AGENTS.md](../AGENTS.md).
  - Break lines and organize hierarchy by information unit.
  - Number completed items.
  - Use checkboxes for acceptance.
  - Issue bodies maintain current effective information.
  - Comments record new information.
  - Record only actual work.
  - Use native issue mentions for related Linear issues.
- Environment policy supplies workspace names, IDs, named owners, and status names.
- “Use a sub-issue for each session” is a replaceable work-granularity preference.
  - It does not prevent users from directly authorizing ordinary work.
  - It does not justify extra issue splitting, waiting for a new issue, or stopping authorized work.
- Environment policy may adjust language, templates, and workflow choices; it cannot add operations the user has not authorized.

### Policy contract

The first version uses Markdown field descriptions read by Agents.
Reuse user-designated policy documents; when none exists, information confirmed in the session can supply necessary mappings.
A policy document need not be inside the package and is not a prerequisite for an ordinary draft.

| Field | Purpose | Needed when |
| --- | --- | --- |
| Scope, version, maintainer | Identify applicable products, Teams, or repos | Using policy |
| Workspace, Team, Project mappings | Locate remote targets | Reading/writing corresponding objects |
| Status meanings and IDs | Map execution, blocking, review, and completion | Changing status |
| Roles and responsibilities | Identify executor, Assignee, reviewer, and acceptance owner | Claiming, dividing, or handing off work |
| Labels, templates, scheduling, session boundaries | Reuse classification and arrange work | Required by the task |
| Language, writing, completion criteria | Override defaults and define acceptance | Explicit policy applies |
| Plans, roles, tool capabilities, verification dates | Determine available native UI, API, and MCP routes | Required capability is constrained |
| GitHub, parent, automation rules | Assess side effects of status changes | Relationship/status operations may trigger them |
| Operations modules, environments, runbook entry points | Locate release, incident, feedback, and maintenance workflows | Modules are enabled |
| Notification recipients and authorized scope | Check message content, destination, and responsibility | Sending external messages |

Resolution steps:

1. Use the applicable policy source explicitly designated by the user.
2. If policies conflict within one scope, identify the current conclusion from effective instructions and explicit versions.
3. Verify IDs, permissions, and automations required by the operation using current tools.
4. If an unresolved value affects the operation, complete independent drafts or reads first, then ask for the specific missing information.

The execution environment manages policy tokens, cookies, and credentials.
The package retains only descriptions of required capabilities and data fields.

## Result reuse and the sole maintained source

Update research, design, and the skill according to the [content maintenance mapping](content-migration.md).
Maintain operating guides, examples, and templates directly in the installation directory.

## Installation and maintenance contract

Install by copying all of `skills/linear-handbook/`, preserving its internal directory structure.
Official Codex documentation lists user `.agents/skills` and repo `.agents/skills` as local discovery locations; the user’s environment and installation instructions determine the actual destination. [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)

- When a skill with the same name already exists, compare its source and user modifications before deciding how to update.
- Replace installed copies with complete versions, first preserving necessary local changes.
- Environment policy stays at its designated location; skill updates do not overwrite it.
- Maintainers edit packaged source; installed copies are delivered versions.
- A user-maintained installation copy is an independent derivative; compare differences before future updates.
- The root README records version, source scope, installation steps, and content entry points.
- Package only the complete skill root; design, validation, and historical material remain project artifacts.

Explicit publishing requirements determine the public repository target, license terms, and plugin release arrangements.
This complete directory supports first-version local installation validation.

## Extension interfaces

- Small teams: update policy roles, review responsibilities, and status mappings.
- Product operations: choose feedback, release, incident, or maintenance workflows according to actual needs.
- New operations workflows: add a reference when inputs, responsibilities, outputs, and acceptance are clear, and add entry-point routing.
- Multiple skills: split a module when it develops independent trigger and maintenance needs.
  - Before splitting, confirm each installation unit can independently obtain required shared rules.
  - Avoid requiring multiple undeclared skills for basic workflows.
- Enterprise governance: preserve questions and boundaries in [extension research](../research/extension-model.md#enterprise-governance), then design when concrete needs arise.

## Validation design

Architecture acceptance follows this document’s decisions, directories, routing, policy, and source mapping.
After assembly, validate the actual usable artifact in this order:

- [ ] Format is valid.
  1. Validate `SKILL.md` frontmatter, naming, and scaffold remnants.
  2. Check the trigger description against task scope.
- [ ] The installation unit is self-contained.
  1. Copy the skill to a temporary location without the original project.
  2. Resolve every local link and confirm it stays inside the installation directory.
  3. Check every section anchor.
  4. Scan for personal IDs, AGENTS dependencies, and signed URLs.
- [ ] Conditional loading supports the main scenarios.
  1. Check policy mapping and minimum configuration in initialization.
  2. Check prerequisites, children, and parent integration acceptance in decomposition.
  3. Check current conclusions and result entry points in updates and handoffs.
  4. Check rereading, deduplication, and stop conditions in conflicts and partial success.
  5. Check that documents actually loaded match the task.
- [ ] Source and installed copies are traceable.
  1. Record file SHA-256 hashes for the tested version.
  2. Check source-to-destination mappings.
  3. Compare file SHA-256 hashes after packaging and installation.

## Sources

The following sources were read on 2026-09-13.
Verification dates bound dynamic official pages; third-party implementations use fixed commits.

- [Agent Skills Specification](https://agentskills.io/specification)
  - Directory structure: skill directory.
  - Frontmatter: required name and description.
  - Progressive disclosure: layered loading.
  - File references: relative references.
- [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)
  - How ChatGPT and Codex use skills: triggering.
  - Where Codex loads local skills: local discovery locations.
  - Distribute skills with plugins: external distribution model.
- [mattpocock README](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/README.md#installation-30-second-setup)
  - Installation: two distribution paths.
- [plugin.json](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/.claude-plugin/plugin.json#L20)
  - skills array: categorized directories and explicit package list.
- [tdd/SKILL.md](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/tdd/SKILL.md#L13)
  - What a good test is: supporting references in the same directory.
- [link-skills.sh](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/scripts/link-skills.sh#L2)
  - Opening comments: restricted to maintainer development use.

## Additional decision: Impeccable structure

Verification and decision date: 2026-09-13.
Feedback source: the user designated `https://github.com/pbakaus/impeccable` as a possible skill-structure reference.
Pinned version: `pbakaus/impeccable@cb56ed6c19a07329a9fa0cd4e657bee040156593`.

### Implementation findings

- One skill entry point maps to multiple command references. [SKILL.src.md](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/skill/SKILL.src.md)
  - The Commands table in `skill/SKILL.src.md` links operating documents.
  - Setup loads the relevant playbook for explicit or implied tasks.
  - `craft-floor.md` loads only when preparing to modify UI.
- Shared content is maintained in `skill/`. [utils.js](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/scripts/lib/utils.js#L199)
  - `readSourceFiles` reads `skill/SKILL.src.md`.
  - `.src.md` prevents installers from mistaking source with unresolved placeholders for installable `SKILL.md`.
- Transformers produce provider differences. [factory.js](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/scripts/lib/transformers/factory.js)
  - `createTransformer` produces platform frontmatter.
  - `compileProviderBlocks` selects platform-specific text.
  - `replacePlaceholders` and script-path substitution produce usable references.
  - Each platform output includes copies of the same references.
- The build converts source into installation artifacts. [build.js](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/scripts/build.js#L698)
  - Runs a transformer for each provider.
  - Release builds can synchronize corresponding installed copies in the root directory.
  - Plugin payloads are assembled from generated skill content.
  - `createAllZips` creates ZIP artifacts.
- Usage and building are separate. [README.md](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/README.md#installation) [package.json](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/package.json)
  - README Installation offers CLI installation.
  - README also offers website ZIP downloads and repository copying.
  - `package.json` uses Bun to run the build script through `build:skills`.

These findings come from reading documentation and code at the pinned version.

### Adoption in this version

1. Retain one entry point at `skills/linear-handbook/` and the existing references/templates directories.
2. Load only the workflows each task needs; give shared writing and policy rules explicit usage conditions.
3. Maintainers edit the sole source, from which packaging and installation copies are produced.
4. Apply fixes from distributed copies to source and regenerate copies; treat independently maintained user copies as derivatives.

The current skill can be copied directly for installation, so `SKILL.md` is both authoritative source and installation entry point.
Impeccable’s `.src.md` prevents accidental installation of source with platform placeholders; this version has none and keeps direct installation.
The existing closed-reference boundary and source-to-destination mapping support these principles directly.

### Conditions for multiple providers

Evaluate a transformation layer only when a requested second platform requires different frontmatter, tool calls, or paths.

- Platform differences need concrete documentation and a reproducible installation problem.
- Keep one shared source and manage platform values centrally.
- Name source files with unresolved placeholders so installers cannot mistake them for installable files.
- Label generated copies with source and version.
- Validate references and installation results separately for each target platform.
- Build tooling should address only confirmed differences and packaging needs.

### Additional sources

All sources below were verified on 2026-09-13; URLs are pinned to the commit above.

- [SKILL.src.md](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/skill/SKILL.src.md)
  - Setup: conditional loading of playbooks and shared quality documents.
  - Commands: command-to-reference mapping at one entry point.
- [utils.js](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/scripts/lib/utils.js#L199)
  - `readSourceFiles` and preceding comments: source directory and `.src.md` naming rationale.
- [factory.js](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/scripts/lib/transformers/factory.js)
  - `createTransformer`: platform frontmatter, placeholder replacement, reference generation.
- [build.js](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/scripts/build.js#L698)
  - Source reading and provider transformation.
  - Root-directory copy synchronization.
  - Plugin and ZIP assembly.
- [README.md](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/README.md#installation)
  - Installation: CLI, ZIP, and repository-copy entry points.
- [package.json](https://github.com/pbakaus/impeccable/blob/cb56ed6c19a07329a9fa0cd4e657bee040156593/package.json)
  - `scripts.build:skills`: Bun build entry point.
