# System Architecture

## High-Level Design

The system is modular, fail-closed by default, and designed for both information/signal generation and (gated) execution.

### Core Components

1. **Data Ingestion Layer**
   - Market data: WebSocket streams + REST fallbacks (Binance, Bybit, OKX, Hyperliquid, etc.)
   - On-chain: RPC + indexers for DeFi metrics
   - Alternative data: Sentiment, news, funding rates, open interest, liquidations

2. **Strategy Layer (per Asset Class)**
   - Pluggable strategy registry
   - Each asset class has specialized modules with enhanced risk filters
   - Composite / ensemble voting with conflict resolution

3. **Risk Engine**
   - Position sizing (Kelly, volatility parity, ATR-based)
   - Multi-level stops (fixed, trailing, time-based, liquidation-aware)
   - Portfolio-level limits (drawdown, concentration, correlation)
   - Circuit breakers and kill switches

4. **Execution & OMS**
   - Smart order routing
   - TWAP/VWAP/Iceberg for large orders
   - Idempotent order submission
   - Paper vs Live adapters (live behind explicit gate)

5. **Security & Audit Layer**
   - See security-architecture.md
   - Every order requires risk-engine token (HMAC-style) before submission

6. **Monitoring & Operations**
   - Real-time dashboards
   - Alerting (Telegram, Slack, PagerDuty)
   - Backtesting + walk-forward validation pipeline

## Data Flow

Market Data → Feature Engineering → Strategy Signals → Risk Checks → Order Intent → Security Gate → Execution Adapter → Exchange

All paths are logged immutably.

## Deployment Patterns

- Containerized (Docker)
- Orchestration: Kubernetes or simple systemd for smaller setups
- Secrets injected at runtime, never baked into images
- Multi-region for latency-sensitive strategies
