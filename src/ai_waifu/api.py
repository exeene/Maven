import openai
from .utils import error_handler

class OpenAIAPI:
    def __init__(self, api_key, max_tokens=150, temperature=0.7):
        openai.api_key = api_key
        self.max_tokens = max_tokens
        self.temperature = temperature

    @error_handler
    def generate_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        return response.choices[0].message.content.strip()