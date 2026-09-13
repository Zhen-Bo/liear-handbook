# Export all filtered data

## Current results

- PR #81 is merged; version [merge-81-abc](fixture://exp-21/merge-81-abc).
- PR review and unit tests passed.
- Lin’s latest acceptance data expects IDs 1–240; actual.csv contains only IDs 1–80, each once.
- IDs 81–240 are missing, 160 records total; full export acceptance failed.
- Evidence: [actual.csv](fixture://exp-21/actual.csv), from the latest comment and acceptance data in requests.md C05.
- Current stage: Implementing/exp-implement, for the missing-record fix.

## Required acceptance

- [ ] 240  records complete, each exactly once.
- [ ] Chinese and newline fields are correct.
- [ ] Include only data readable by the current user.

## Next steps

1. Open the export query path in merge-81-abc; compare actual.csv IDs with query responses stage by stage to locate missing data.
2. Fix missing records using traceable evidence; rerun the same 240 records and check count, ID set, and duplicates.
3. Check Chinese, newline, and permission cases; link each result to the tested version before declaring completion.

## Relations and workflow

- Parent EXP-20: Implementing, waiting for this required export artifact.
- Merge automation using a PR closing relation set this issue to Done before product acceptance.
- The automation settings maintainer should check whether to map merging to acceptance; current tools only support issue updates.
