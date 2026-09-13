# Execution order

1. Agent A completes contract.md.
2. The maintainer reviews the contract.
3. Start implementation once the contract is usable.
   - Agent A: backend.md.
   - Agent B: frontend.md.
4. The maintainer reviews one item at a time.
5. Agents prioritize rework.
6. Once both implementations are usable, A completes integration.md.
7. Check outcomes against the overall acceptance in parent-feature.md.

## Capacity and allocation

- Each Agent executes one item at a time.
- The aggregate parent does not occupy another execution slot.
- Deliverables awaiting review still count toward WIP.
- Do not open new work before review capacity is released.
- Backend waits for the shared contract.
- Frontend waits for the shared contract.
- Backend and frontend have no artifact dependency on each other.
- Integration waits for the backend artifact.
- Integration waits for the frontend artifact.
- A alone maintains src/app/export.ts.
- Determine artifact dependencies from actual required inputs.
- This round uses corresponding filenames as work identifiers.
