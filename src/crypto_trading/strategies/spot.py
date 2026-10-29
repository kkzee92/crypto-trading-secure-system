"""Spot market strategies with enhancements."""

from typing import Optional
from ..core.engine import Signal


class SpotMomentumStrategy:
    asset_class = "spot"

    def __init__(self, fast: int = 10, slow: int = 30, min_confidence: float = 0.6):
        self.fast = fast
        self.slow = slow
        self.min_confidence = min_confidence

    def generate_signal(self, market_data: dict) -> Optional[Signal]:
        prices = market_data.get("closes", [])
        if len(prices) < self.slow:
            return None
        fast_ma = sum(prices[-self.fast:]) / self.fast
        slow_ma = sum(prices[-self.slow:]) / self.slow
        if fast_ma > slow_ma * 1.002:  # small buffer
            confidence = min(0.9, (fast_ma / slow_ma - 1) * 50)
            if confidence < self.min_confidence:
                return None
            return Signal(
                symbol=market_data.get("symbol", "BTCUSDT"),
                side="buy",
                size=0.01,  # fractional; risk engine will further constrain
                asset_class=self.asset_class,
                confidence=confidence,
                metadata={"fast_ma": fast_ma, "slow_ma": slow_ma},
            )
        return None
