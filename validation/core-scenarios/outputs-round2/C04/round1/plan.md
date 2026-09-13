# Execution order

1. Agent A completes contract.md first; the maintainer reviews the contract.
2. Once the contract is usable, A handles backend.md and B handles frontend.md.
3. The maintainer reviews one item at a time; the other pending item still counts toward WIP. Agents prioritize rework and do not start another item.
4. Once both implementations are usable, A alone maintains src/app/export.ts and completes integration.md.
5. Check outcomes against the overall acceptance in parent-feature.md.

- Each Agent executes one item at a time; the aggregate parent does not occupy another slot.
- Backend and frontend wait for the shared contract and have no artifact dependency on each other.
- Integration waits for both implementations.
- Assigning a sole writer prevents shared-entry conflicts; artifact dependencies follow actual inputs.
- This round is planning; the filenames above identify work. Actual Team, status IDs, and new issue IDs were not supplied.
