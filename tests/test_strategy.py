import unittest
from unittest.mock import patch
from src.ai_waifu.strategy import TradingStrategy

class TestTradingStrategy(unittest.TestCase):
    @patch('src.ai_waifu.utils.load_config')
    def test_strategy_loading(self, mock_load):
        mock_load.return_value = {
            "test_strategy": "Test strategy details"
        }
        strategy = TradingStrategy("dummy.json")
        self.assertEqual(strategy.get_strategy("test_strategy"), "Test strategy details")
        
    def test_missing_strategy(self):
        with patch('src.ai_waifu.utils.load_config') as mock_load:
            mock_load.return_value = {}
            strategy = TradingStrategy("dummy.json")
            self.assertIn("No strategy found", strategy.get_strategy("missing"))

if __name__ == '__main__':
    unittest.main()