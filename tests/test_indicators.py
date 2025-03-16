import unittest
from src.indicators import TechnicalIndicators

class TestIndicators(unittest.TestCase):
    def setUp(self):
        self.indicators = TechnicalIndicators(period_sma=5, period_rsi=5)
        self.indicators.prices.extend([100, 102, 101, 103, 104])

    def test_sma(self):
        self.assertAlmostEqual(self.indicators.sma(), 102.0)

    def test_rsi(self):
        self.assertGreaterEqual(self.indicators.rsi(), 0)
        self.assertLessEqual(self.indicators.rsi(), 100)

if __name__ == "__main__":
    unittest.main()