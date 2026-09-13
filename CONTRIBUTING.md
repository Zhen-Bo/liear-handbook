# Contributing

## Report a problem

Choose a bug report or improvement proposal in [GitHub Issues](https://github.com/Zhen-Bo/liear-handbook/issues/new/choose).
For general usage questions, open a blank issue.

- Describe the original request and expected outcome.
- Include relevant file paths or actual output.
- For behavior issues, include the skill version and steps to reproduce.
- Remove private Workspace data and sensitive information before sharing.

## Make changes

1. Read the writing and maintenance rules in [AGENTS.md](AGENTS.md).
2. Update the appropriate source using the [maintenance guide](docs/maintenance.md).
3. Support feature facts with official sources, section names, and verification dates.
4. Run the affected checks and record their results.
5. Describe the problem solved and verification evidence in the pull request.

For substantial architecture or workflow changes, first open an issue describing the goal, scope, and proposed approach.
Small documentation fixes can go directly into a pull request.

## Verification

Markdown link checks use Python and `markdown-it-py`.

```bash
python -m pip install markdown-it-py
python validation/check_skill_links.py skills/linear-handbook
python validation/check_repository_links.py .
```

For workflow or template changes, also verify the affected scenarios.
See the [validation guide](validation/README.md) for historical cases and replay instructions.

## License

Project content is licensed under the [MIT License](LICENSE).
When adding third-party excerpts or adaptations, retain the applicable attribution and license notices and update the [source notes](docs/sources-and-attribution.md).
