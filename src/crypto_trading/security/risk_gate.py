"""Risk gate — cryptographic-style approval required before any order."""

from typing import Optional
import hashlib
import hmac
import os
import time

from ..core.engine import Signal


class RiskGate:
    """Fail-closed risk approval. Issues short-lived tokens."""

    def __init__(self, secret: Optional[bytes] = None):
        self.secret = secret or os.urandom(32)

    def approve(self, signal: Signal) -> bool:
        """Basic risk checks. Extend with position limits, drawdown, etc."""
        if signal.size <= 0 or signal.confidence < 0.5:
            return False
        if signal.asset_class == "futures" and signal.size > 0.1:  # example limit
            return False
        # Issue token (in real system this would be verified by execution layer)
        token = self._issue_token(signal)
        return token is not None

    def _issue_token(self, signal: Signal) -> Optional[str]:
        payload = f"{signal.symbol}|{signal.side}|{signal.size}|{int(time.time())}"
        signature = hmac.new(self.secret, payload.encode(), hashlib.sha256).hexdigest()
        return f"{payload}|{signature}"
