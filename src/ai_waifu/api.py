import openai
from typing import Optional
from .utils import error_handler

class OpenAIAPI:
    def __init__(
        self,
        api_key: str,
        max_tokens: int = 150,
        temperature: float = 0.7,
        model: str = "gpt-3.5-turbo"
    ):
        if not api_key.startswith("sk-"):
            raise ValueError("Invalid OpenAI API key format")
        
        openai.api_key = api_key
        self.max_tokens = max(50, min(max_tokens, 2048))  # Clamp values
        self.temperature = max(0.0, min(temperature, 2.0))
        self.model = model

    @error_handler
    def generate_response(self, prompt: str) -> Optional[str]:
        """Generate response with safe prompt handling."""
        if len(prompt) > 4096:
            raise ValueError("Prompt exceeds maximum length of 4096 characters")
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )
        return response.choices[0].message.content.strip() if response.choices else None