import unittest
from unittest.mock import patch, MagicMock
from src.ai_waifu.waifu import AIWaifu

class TestAIWaifu(unittest.TestCase):
    @patch('src.ai_waifu.waifu.load_config')
    def setUp(self, mock_load_config):
        mock_load_config.return_value = {
            "openai_api_key": "test_key",
            "character_config": "test_character.json",
            "strategy_config": "test_strategies.json",
            "max_tokens": 150,
            "temperature": 0.7
        }
        self.waifu = AIWaifu("config.json")

    def test_initialization(self):
        self.assertIsNotNone(self.waifu.character)
        self.assertIsNotNone(self.waifu.strategy)
        self.assertIsNotNone(self.waifu.api)

    @patch('src.ai_waifu.api.OpenAIAPI.generate_response')
    def test_interact(self, mock_generate):
        mock_generate.return_value = "Test response"
        response = self.waifu.interact("Hello")
        self.assertEqual(response, "Test response")

if __name__ == '__main__':
    unittest.main()