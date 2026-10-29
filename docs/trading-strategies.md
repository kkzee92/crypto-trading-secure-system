# Enhanced Trading Strategies by Asset Class

## Spot Markets

### Core Strategies
- **Momentum / Trend Following**: Moving average crossovers, breakout with volume confirmation. Enhancement: regime filter (HMM or ADX) to avoid ranging markets.
- **Mean Reversion**: Bollinger Band + RSI. Enhancement: volatility-adjusted entry thresholds.
- **Dollar-Cost Averaging (DCA)**: Scheduled buys. Enhancement: dynamic allocation based on drawdown or volatility.
- **Grid Trading**: Range-bound grids. Enhancement: adaptive grid spacing using ATR; auto-pause on trend breakout.

### Enhancements
- Position sizing via volatility parity or fractional Kelly
- Correlation filter vs BTC/ETH
- Liquidity score gate (min volume / order book depth)

## Futures & Perpetuals

### Core Strategies
- **Funding Rate Arbitrage**: Long/short based on extreme funding. Enhancement: multi-exchange funding differential + basis monitoring.
- **Trend Following with Leverage**: Controlled leverage (max 2-5x depending on volatility). Enhancement: liquidation buffer (maintain >20% margin buffer).
- **Basis Trading**: Cash-and-carry. Enhancement: funding-aware entry/exit.

### Enhancements
- Dynamic leverage based on realized volatility and funding
- Forced deleverage triggers
- Open interest and liquidation heatmap filters

## Options

### Core Strategies
- **Volatility Selling**: Iron condors / strangles in high IV rank. Enhancement: delta-neutral hedging automation.
- **Covered Calls / Protective Puts**: Overlay on spot holdings.
- **Directional with Greeks Control**: Limited risk via defined-risk structures.

### Enhancements
- IV Rank / IV Percentile filters
- Greeks exposure limits (delta, vega, gamma)
- Early assignment / expiration risk management

## DeFi / Yield

### Core Strategies
- **Liquidity Provision**: Concentrated liquidity (Uniswap V3 style) with range management.
- **Yield Farming / Staking**: Multi-protocol allocation.
- **Cross-DEX / Cross-chain Arbitrage**.

### Enhancements
- Impermanent loss estimators and hedges
- Smart contract risk scoring (audit status, TVL, age, exploit history)
- Gas-optimized rebalancing
- Oracle manipulation detection

## Stablecoins

### Core Strategies
- **Peg Monitoring & Depeg Arbitrage**: Buy discount / sell premium to peg.
- **Yield Optimization**: Across lending protocols with risk-adjusted returns.

### Enhancements
- Reserve transparency and attestation checks
- Redemption risk and blacklisting monitoring
- Diversification across issuers

## Altcoins / Low-Cap

### Core Strategies
- **Momentum Rotation**: Relative strength vs BTC/ETH.
- **Narrative / Catalyst Tracking**: Event-driven.

### Enhancements
- Strict liquidity and market-cap filters
- Higher stop-loss and smaller position sizes
- Correlation and beta monitoring
- Avoid illiquid pairs during high volatility

## Cross-Cutting Enhancements

- Ensemble / voting across strategies
- Walk-forward and out-of-sample validation required before live consideration
- Regime detection (bull, bear, ranging, high-vol) to enable/disable strategy families
- All strategies output signals only; risk engine has final authority

## Implementation Notes

Strategies live in `src/crypto_trading/strategies/`. Each must implement a standard interface and declare its asset class, risk parameters, and required data feeds.
