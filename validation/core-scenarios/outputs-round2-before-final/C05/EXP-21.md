# Export all filtered data

## Current results

- PR #81 is merged.
- Artifact version: [merge-81-abc](fixture://exp-21/merge-81-abc).
- PR review passed.
- Unit tests passed.
- Lin’s latest acceptance data
  - Expected IDs: 1–240.
  - Actual.csv IDs: 1–80.
  - Each actual ID appears once.
- Missing IDs: 81–240.
- Missing count: 160.
- Full export acceptance failed.
- Acceptance evidence: [actual.csv](fixture://exp-21/actual.csv).
- Data source: latest acceptance summary in requests.md C05.
- Current stage: Implementing/exp-implement.
- Follow-up work: fix missing records.

## Required acceptance

- [ ] The export contains all 240 records.
- [ ] Each record appears exactly once.
- [ ] Chinese fields are correct.
- [ ] Newline fields are correct.
- [ ] Include only data readable by the current user.

## Next steps

1. Open the export query path in merge-81-abc.
2. Compare actual.csv IDs with query responses stage by stage to locate missing data.
3. Fix missing records based on evidence.
4. Rerun export with the same 240 records.
5. Check ID-set completeness.
6. Check occurrences of each ID.
7. Check Chinese fields.
8. Check newline fields.
9. Check permission cases.
10. Save individual results tied to the tested version.
11. Determine completion from all required acceptance criteria.

## Relations and workflow

- Parent EXP-20: Implementing.
- Parent waits for this required export artifact.
- Merge automation using a PR closing relation set this issue to Done.
- Automatic closure preceded product acceptance.
- The settings maintainer should check whether to map merging to acceptance.
- Current tools support issue updates only.
