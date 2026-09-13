Source: requests.md → C01

Blank initialization

User request: I just created a Workspace and want to use Linear to manage a personal expense web app with two Agents. The first version should accept expense amounts and categories, show this month’s total, and retain data after refresh. Prepare a minimal environment configuration, Project brief, and initial issues ready for handoff. You may create the Project and issues in this simulation.

- Workspace: Pocket, ID ws-pocket, Free.
- The native interface created the same-name default Team: Pocket, ID team-pocket, identifier PKT, time zone Asia/Taipei.
- Acting identity: Owner, ID user-owner, the human outcome owner.
- Agents: external sessions A and B share the Owner connection and can both access Pocket.
- Statuses: Backlog / backlog / st-backlog; Todo / unstarted / st-todo; Doing / started / st-doing; Done / completed / st-done; Canceled / canceled / st-canceled.
- Default status: st-backlog.
- All Project search results: empty.
- All issue search results: empty.
- Labels: empty.
- Estimates: off.
- Cycles: off.
- Automations: PR, parent/sub-issue, auto-close, and auto-archive are all off.
- Owner’s notification entry point: Inbox, checked daily; subscribes to owned issues.
- Requirement decisions: localStorage in one browser; positive integer TWD expenses; Food/Transport/Other categories; version 1 only supports addition and monthly total.
- Environment: an empty Vite + TypeScript repository pocket-web exists, version fixture-base-01, test tool Vitest.
- Simulated tools can read the above data, create a Project and issues, and read back new objects; no Workspace/Team/settings creation tools are provided.
