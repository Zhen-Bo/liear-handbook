# Bug issue body template

For correcting actual behavior that deviates from promised behavior.
Classification: [Work type guide — Bug](../../references/issue-types.md#bug).

## Usage

1. Enter the title in the issue title field.
2. Copy the concise version as the issue body and replace `{…}`.
3. For multiple affected scenarios, add the environment and acceptance criteria for each.
4. After filling in the template, remove empty fields and instructions that no longer serve a purpose.

Include only environment fields relevant to reproduction.
Prefer the target project's existing issue template.
Redact personal data and credentials in evidence first.
When the root cause is unknown, describe the observable failure.
If hypotheses must be retained, list supporting evidence and questions to verify separately.

## Concise version

Title: `Fix {observable error} when {trigger scenario}`

```markdown
## Problem

{Which task is blocked for the affected users, and how.}

- Actual: {Observed result.}
- Expected: {Promised result.}
- Basis: {Link and section in the specification or existing acceptance criteria.}

## Environment

- Product version: {Version or commit.}
- Operating system: {System and version.}
- Runtime environment: {Relevant browser, runtime, or device version.}

## Setup

- {Configuration, account state, or test data required to reproduce the issue.}

## Reproduction steps

1. {Action.}
2. {Action that triggers the error.}

## Scope

- {Behavioral boundary of this fix.}

## Acceptance

- [ ] {Observable expected result in the original failing scenario.}
- [ ] {Specific regression result for the affected path.}

## Evidence

- {Failure record location and observation time.}
```

## Completed example

This fictional product example shows a completed problem statement and acceptance criteria.

Title: `Fix the persistent loading screen when a password reset link has expired`

```markdown
## Problem

Users who open an expired password reset link cannot tell that it is no longer valid.

- Actual: The page keeps displaying "Loading".
- Expected: Display "This link has expired. Please request a new one."
- Basis: The "Password reset link expiration" requirement specifies that reset links expire 30 minutes after creation.

## Environment

- Product version: Web 1.8.2.
- Operating system: Windows 11.
- Browser: Chrome 128.

## Setup

- The test account has a reset link issued 31 minutes ago.

## Reproduction steps

1. Open the reset link in a browser that is not signed in.
2. Wait for the reset API to return 410 and TOKEN_EXPIRED.

## Scope

- Handle the display state when the password reset page receives TOKEN_EXPIRED.

## Acceptance

- [ ] An expired link displays "This link has expired. Please request a new one."
  1. Open a link issued 31 minutes ago.
  2. Confirm that the API returns TOKEN_EXPIRED.
  3. Confirm that the loading screen disappears and the expiration message appears.
- [ ] A valid link still allows a password reset.
  1. Open a link issued 5 minutes ago.
  2. Set a new password that meets the password rules.
  3. Sign in successfully with the new password.

## Evidence

- Requirement record: "Password reset link expiration".
- Failure record: Attachment expired-reset.har, request /password/reset/validate.
- Observation time: 2026-09-10 10:20 UTC+8.
```

## Configuration notes

### Feature facts

Verified on: 2026-09-13.

- A Standard template can prefill issue properties and the description.
  - Source: [Linear Issue templates — Create standard issue templates](https://linear.app/docs/issue-templates#create-standard-issue-templates).
- A Form template can make fields required.
  - Source: [Linear Issue templates — Create form templates](https://linear.app/docs/issue-templates#create-form-templates).

### Recommendations

- Use this file's concise version as the starting point for the body.
- Use a Form template for information that must be provided at creation.
- After fixing the issue, add links to actual verification in the evidence section.
- Use permalinks to fixed versions for code evidence.


## Writing defaults

Follow [writing](../../references/writing.md) for formatting, evidence, and the issue's current conclusions.
