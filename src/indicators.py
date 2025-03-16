from collections import deque
import numpy as np

class TechnicalIndicators:
    def __init__(self, period_sma: int = 14, period_rsi: int = 14):
        self.prices = deque(maxlen=period_sma)
        self.period_sma = period_sma
        self.period_rsi = period_rsi

    def sma(self) -> float:
        return sum(self.prices) / len(self.prices) if self.prices else 0

    def ema(self, alpha: float = 0.5) -> float:
        if not self.prices:
            return 0
        ema_prev = self.prices[0]
        for price in list(self.prices)[1:]:
            ema_prev = alpha * price + (1 - alpha) * ema_prev
        return ema_prev

    def rsi(self) -> float:
        if len(self.prices) < self.period_rsi:
            return 0
        deltas = np.diff(list(self.prices))
        gains = deltas[deltas > 0].mean() if any(deltas > 0) else 0
        losses = -deltas[deltas < 0].mean() if any(deltas < 0) else 0
        rs = gains / losses if losses != 0 else 0
        return 100 - (100 / (1 + rs))

    def macd(self, short_period: int = 12, long_period: int = 26) -> float:
        if len(self.prices) < long_period:
            return 0
        short_ema = self._calculate_ema(short_period)
        long_ema = self._calculate_ema(long_period)
        return short_ema - long_ema

    def _calculate_ema(self, period: int) -> float:
        alpha = 2 / (period + 1)
        prices = list(self.prices)[-period:]
        ema_prev = prices[0]
        for price in prices[1:]:
            ema_prev = alpha * price + (1 - alpha) * ema_prev
        return ema_prev