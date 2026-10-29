# Security Policy

## Supported Versions
Only the latest commit on `main` receives security updates. This is a reference implementation.

## Reporting a Vulnerability
Please **do not** open a public issue. Use GitHub's private vulnerability reporting form (Security tab → Advisories).

Include reproduction steps. Use only synthetic data. Expect acknowledgement within 7 days (best-effort).

## In Scope
- Trading engine, strategy modules, risk engine
- Security controls, CI gates, secret handling patterns
- Any path that could allow unauthorized order submission or secret leakage

## Out of Scope
- Exchange or protocol vulnerabilities themselves
- Physical security of operator hardware

## Built-in Protections
- Secret scanning in CI
- No secrets in repository
- Fail-closed paper mode by default
- Risk-engine approval required for order submission
- Licence and dependency controls
