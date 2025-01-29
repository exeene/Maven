import unittest
from unittest.mock import patch
from src.ai_waifu.character import Character

class TestCharacter(unittest.TestCase):
    @patch('src.ai_waifu.utils.load_config')
    def test_character_creation(self, mock_load):
        mock_load.return_value = {
            "name": "Test",
            "personality": "testy",
            "interaction_style": "formal"
        }
        character = Character("dummy_path.json")
        self.assertEqual(character.name, "Test")
        self.assertEqual(character.personality, "testy")
        
    def test_default_values(self):
        with patch('src.ai_waifu.utils.load_config') as mock_load:
            mock_load.return_value = {}
            character = Character("dummy.json")
            self.assertEqual(character.name, "AI Waifu")

if __name__ == '__main__':
    unittest.main()