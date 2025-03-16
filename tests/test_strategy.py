import unittest
from src.strategy import TradingStrategy

class TestStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = TradingStrategy(capital=1000)

    def test_should_buy(self):
        self.assertFalse(self.strategy.should_buy(105))  # Пример условия

if __name__ == "__main__":
    unittest.main()