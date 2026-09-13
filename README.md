<p align="center">
  <img src="assets/readme-hero.svg" alt="Linear handbook — Practical guides for Linear" width="1200">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-007EC6?style=flat" alt="License MIT"></a>
  <a href="https://github.com/Zhen-Bo/liear-handbook/releases"><img src="https://img.shields.io/github/v/release/Zhen-Bo/liear-handbook?style=flat&amp;label=version&amp;color=0E7490&amp;include_prereleases" alt="Latest release version"></a>
  <a href="https://skills.sh/Zhen-Bo/liear-handbook"><img src="https://skills.sh/b/Zhen-Bo/liear-handbook" alt="skills.sh installs"></a>
  <a href="https://openai.com/index/gpt-6-astra/"><img src="assets/made-for-astra.svg" alt="For OpenAI Astra"></a>
</p>

A Linear skill for individual developers and Agents that turns requests into work you can advance, verify, and hand off.

- **Break work into deliverable units**: organize parents, sub-issues, and necessary dependencies around outcomes.
- **Make progress easy to pick up**: issue bodies retain current conclusions, while comments record new information.
- **Apply consistent rules**: planning, writing, acceptance, and tool recovery share the same workflows and templates.

[Quick start](#quick-start) · [Installation](#installation) · [Guides](#guides) · [Templates](#templates) · [Report a problem](#feedback-and-changes)

## Quick start

After installing and enabling the skill, give your Agent this request:

```text
Use the linear-handbook skill for the following request.

Project managers need to export the currently filtered tasks as CSV, preserving the list order.
Draft a parent issue and split it into sub-issues with independently deliverable outcomes.
For each sub-issue, list its scope, acceptance criteria, and required prior deliverables.
For this request, provide drafts in your response only.
```

The result should include overall acceptance criteria for the parent and the scope and dependencies of each sub-issue.
Here is a decomposition from the [complete example](skills/linear-handbook/references/feature-decomposition.md):

```text
Let project managers export the currently filtered tasks
├── Define the download contract
├── Produce correct CSV from the endpoint    ← Uses the download contract
├── Implement the interface to the contract  ← Uses the download contract
└── Integrate the full download flow         ← Requires endpoint and interface deliverables
```

> [!TIP]
> When reviewing the draft, check that each sub-issue has an assessable outcome and the parent retains acceptance criteria for the complete export.
> Adapt the decomposition to the requirements and existing deliverables.

## Installation

Requires Node.js and the `npx` command provided by npm.

```bash
npx skills add Zhen-Bo/liear-handbook
```

Follow the CLI prompts to select the installation target, then use the draft example above to confirm the skill loads.
See the [skills.sh documentation](https://skills.sh/docs/cli) for CLI usage.

<details>
<summary>Manual installation or direct loading</summary>

1. Copy the complete `skills/linear-handbook/` directory into a skills directory supported by your environment.
2. Enable `linear-handbook` using that environment's loading mechanism.
3. Run the draft example above to confirm the Agent can find the workflows and templates.

Preserve this installation structure:

```text
linear-handbook/
├── SKILL.md
├── references/
└── assets/
    └── templates/
```

For direct loading, ask the Agent to start at `SKILL.md` and provide read access to its supporting documents.

</details>

To operate Linear directly, the environment must provide the relevant tools and access.
Record your actual Workspace, Team, and status mappings in your own [environment policy](skills/linear-handbook/references/policy.md).
Use an existing policy when one is available.

---

## Guides

After enabling the skill, describe the outcome you want.

| Task | Example request | Guide |
| --- | --- | --- |
| Initialize an environment | Review the existing Workspace and configure what this project needs | [Environment setup](skills/linear-handbook/references/workspace-setup.md) |
| Create a project | Build a Project brief, Milestones, and initial work from product requirements | [Project planning](skills/linear-handbook/references/project-planning.md) |
| Break down work | Split this request into independently verifiable deliverables and identify necessary dependencies | [Issue decomposition](skills/linear-handbook/references/issue-decomposition.md) |
| Maintain bodies and comments | Put current conclusions in the body and record new information in a comment | [Writing rules](skills/linear-handbook/references/writing.md) |
| Verify and hand off | Check the deliverables against acceptance criteria and prepare entry points for the next Agent | [Issue lifecycle](skills/linear-handbook/references/issue-lifecycle.md) |
| Coordinate multiple Agents | Confirm work assignments and resolve conflicts between Agents editing the same deliverable | [Coordination](skills/linear-handbook/references/multi-agent-coordination.md) |
| Recover tool operations | Issue creation timed out; check the result before deciding what to do next | [Tool recovery](skills/linear-handbook/references/tool-recovery.md) |

[SKILL.md](skills/linear-handbook/SKILL.md) routes tasks to the complete workflows.
Feature descriptions retain official sources and verification dates in the relevant documents; check current tools and context when acting.

## Templates

| Type | Purpose |
| --- | --- |
| [Bug](skills/linear-handbook/assets/templates/bug.md) | Affected version, environment, reproduction steps, and fix acceptance |
| [Feature](skills/linear-handbook/assets/templates/feature.md) | User need, delivery scope, and acceptance |
| [Research](skills/linear-handbook/assets/templates/research.md) | Questions, decision criteria, and evidence |
| [Refactor](skills/linear-handbook/assets/templates/refactor.md) | Structural changes and preservation of external behavior |
| [Migration](skills/linear-handbook/assets/templates/migration.md) | Cutover conditions, data verification, and recovery |
| [Project brief](skills/linear-handbook/assets/templates/project-brief.md) | Project goal and delivery stages |
| [Project update](skills/linear-handbook/assets/templates/project-update.md) | Overall progress, risks, and next steps |
| [Progress comment](skills/linear-handbook/assets/templates/progress-comment.md) | New findings, decision reasons, and deliverables |
| [Handoff](skills/linear-handbook/assets/templates/handoff.md) | Existing deliverables and entry points for continuing work |

---

## Further reading

To review the skill, read these in order:

1. [Entry point](skills/linear-handbook/SKILL.md): check task routing.
2. [Writing rules](skills/linear-handbook/references/writing.md): check content selection and structure.
3. [Project setup example](skills/linear-handbook/references/project-bootstrap.md): review a complete workflow.

Consult research and design documents when tracing evidence or changing the architecture.

| Directory | Contents and entry points |
| --- | --- |
| `skills/linear-handbook/` | Installable guides, examples, and templates |
| `research/` | [Research scope, sources, and adoption rationale](research/scope-and-sources.md) |
| `design/` | [Architecture decisions](design/skill-architecture.md) and [content mapping](design/content-migration.md) |
| `validation/` | [Check scripts, fixed cases, and validation records](validation/README.md) |
| `docs/` | [Maintenance guide](docs/maintenance.md) and [source notes](docs/sources-and-attribution.md) |
| `assets/` | README images |

## Feedback and changes

Report usage problems, documentation errors, and ideas through [GitHub Issues](https://github.com/Zhen-Bo/liear-handbook/issues).
Include enough information to reproduce or assess the problem:

- File path and relevant section.
- Original request and expected outcome.
- Actual output or operation result.
- Relevant environment and tool information.

Remove private Workspace data and sensitive information before sharing.

See the [contribution guide](CONTRIBUTING.md) for the change process and submission requirements.

## Sources and license

See [sources and acknowledgments](docs/sources-and-attribution.md) for feature research and structural references.
Source excerpts retain their attribution and licensing information.
This project uses the [MIT License](LICENSE).
