import unittest
from unittest.mock import patch, MagicMock
from maven.llm_integration.openai_client import OpenAIAPI

class TestOpenAIAPI(unittest.TestCase):
    def setUp(self):
        self.api = OpenAIAPI("test_key", 150, 0.7)

    @patch('openai.ChatCompletion.create')
    def test_successful_response(self, mock_create):
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Test response"
        mock_create.return_value = mock_response
        
        response = self.api.generate_response("Test prompt")
        self.assertEqual(response, "Test response")

    @patch('openai.ChatCompletion.create')
    def test_error_handling(self, mock_create):
        mock_create.side_effect = Exception("API Error")
        response = self.api.generate_response("Test")
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()