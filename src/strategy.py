from .indicators import TechnicalIndicators

class TradingStrategy:
    def __init__(self, capital: float, risk_per_trade: float = 0.01):
        self.capital = capital
        self.risk_per_trade = risk_per_trade
        self.indicators = TechnicalIndicators()

    def should_buy(self, current_price: float) -> bool:
        rsi = self.indicators.rsi()
        sma = self.indicators.sma()
        return rsi < 30 and current_price < sma

    def should_sell(self, current_price: float) -> bool:
        rsi = self.indicators.rsi()
        sma = self.indicators.sma()
        return rsi > 70 and current_price > sma