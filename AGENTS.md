# Agent Rules for AI Coding Assistants

These rules apply to any AI coding agent working in this repository.

## Core Principles
1. **Never commit secrets**, API keys, private keys, mnemonics, or real personal data.
2. **Paper / simulation mode is the default.** Live trading code paths must remain behind explicit gates.
3. **Risk engine has final authority.** Strategies generate signals only.
4. Prefer stdlib or well-audited dependencies. Justify any new dependency.
5. All changes must pass CI gates (lint, tests, secret scan, licence check).
6. Human review is required before merge.

## Prohibited
- Pasting production keys or real customer data into prompts or code
- Disabling risk checks or kill switches
- Adding withdraw permissions to exchange API key examples
- Committing `.env` files or hard-coded credentials

## Required Practices
- Use synthetic or public fixtures only
- Document AI assistance in commit messages or PR template when significant
- Keep strategy logic pure and testable offline where possible
- Update docs when architecture or security controls change

## Definition of Done
CI green + human review + no secret findings + documentation updated if needed.
