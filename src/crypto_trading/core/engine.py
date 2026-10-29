"""Core trading engine — fail-closed, signal-to-order pipeline."""

from typing import Protocol, Optional
from dataclasses import dataclass


@dataclass
class Signal:
    symbol: str
    side: str  # "buy" | "sell"
    size: float
    asset_class: str
    confidence: float
    metadata: dict


class Strategy(Protocol):
    asset_class: str

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        ...


class TradingEngine:
    """Orchestrates strategies → risk → (paper) execution."""

    def __init__(self, risk_gate, mode: str = "paper"):
        self.risk_gate = risk_gate
        self.mode = mode  # "paper" or "live" (live requires extra gates)
        self.strategies: list[Strategy] = []

    def register_strategy(self, strategy: Strategy) -> None:
        self.strategies.append(strategy)

    def run_cycle(self, market_data: dict) -> list[dict]:
        """Run one decision cycle. Returns order intents (paper by default)."""
        intents = []
        for strat in self.strategies:
            signal = strat.generate_signal(market_data)
            if signal is None:
                continue
            if not self.risk_gate.approve(signal):
                continue
            intent = {
                "symbol": signal.symbol,
                "side": signal.side,
                "size": signal.size,
                "mode": self.mode,
                "strategy": type(strat).__name__,
            }
            intents.append(intent)
            # In paper mode we log only; live would require additional approval
        return intents
