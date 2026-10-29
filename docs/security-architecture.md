# Cyber & Data Security Architecture

## Principles

- **Zero Trust**: Verify every request; assume breach
- **Least Privilege**: API keys and roles have minimal permissions
- **Defense in Depth**: Multiple independent controls
- **Fail Closed**: Default deny; live trading requires explicit multi-factor approval
- **No Secrets in Code/Git**: Enforced by CI (gitleaks + custom scans)
- **Auditability**: Immutable, append-only logs for all decisions and orders

## Key Management

- Exchange API keys: scoped (trade only, no withdraw), IP-whitelisted, rotated on schedule or incident
- Wallet keys (DeFi): hardware wallet or HSM; never on hot servers for large balances
- Internal signing keys for risk tokens: rotated, stored in vault
- Secrets: HashiCorp Vault, AWS Secrets Manager, or equivalent; short-lived credentials preferred

## Encryption & Data Protection

- **In Transit**: TLS 1.3 minimum; certificate pinning where feasible
- **At Rest**: AES-256 for configuration stores, databases, logs containing sensitive data
- **PII / Personal Data**: Minimized; synthetic fixtures only in this repo (PDPA-style guard)
- **Key Rotation**: Automated where possible; documented procedures

## Access Control & Authentication

- Role-based access control (RBAC): Trader, Risk Manager, Auditor, Operator
- MFA mandatory for production access and live-mode toggles
- Session timeouts and anomaly detection on login patterns
- Just-in-time access for emergency overrides (logged and reviewed)

## CI/CD & Supply Chain Security

- Secret scanning (gitleaks) on every PR and push, including full history
- Dependency scanning + Dependabot
- Licence allow-list
- Signed commits recommended
- Immutable builds; no floating tags in production

## Runtime Protections

- Order submission requires valid risk-engine approval token (cryptographic)
- Rate limiting and anomaly detection on order volume / price deviation
- Kill switch accessible to risk managers (immediate halt of new orders)
- Paper/simulation mode is the default; live mode is gated and monitored
- Sandbox / testnet first for all strategy changes

## Monitoring, Detection & Response

- Real-time monitoring of positions, PnL, order flow, API errors
- Anomaly rules: unusual size, off-hours activity, failed risk checks spike
- Incident response playbook: isolate, rotate keys, freeze trading, post-mortem
- Regular penetration testing and tabletop exercises recommended

## Compliance Considerations

- Local regulatory requirements (KYC/AML where applicable, reporting)
- Data residency for logs if required
- This system is a technical reference; operators are responsible for legal compliance

## Reporting Vulnerabilities

Use GitHub private vulnerability reporting. Do not open public issues for security problems.
