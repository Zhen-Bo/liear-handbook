# Connect the real export service and verify browser CSV downloads

## Inputs and scope

- Blocked by: usable implementation and verification versions from backend.md and frontend.md.
- Executor: Agent A.
- Sole shared-entry writer: Agent A, src/app/export.ts.
- Delivery location: verification/csv-export.md and the integration version.
- Connect the complete query and interface; run all overall acceptance checks in parent-feature.md.

## Acceptance

- [ ] The actual browser download matches every record in the known complete readable set.
- [ ] Special characters, sorting, permissions, and 0/5000/5001 boundaries match the parent.
- [ ] Each result identifies the integration version and actual data baseline.
- [ ] Mark the overall outcome complete only after all required parent acceptance criteria pass.

## Next steps

1. Check the actual backend/frontend entry points and contract versions.
2. Connect src/app/export.ts, prepare multi-page data, and perform browser acceptance.
