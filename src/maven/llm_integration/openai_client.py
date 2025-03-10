import openai
import time
import json

class OpenAIAPI:
    def __init__(self, config_path="configs/config.json"):
        """Initialize OpenAI API client with rate limiting."""
        self.load_config(config_path)
        self.last_request_time = 0
    
    def load_config(self, path):
        """Load API key and rate limit from config file."""
        with open(path, "r") as file:
            config = json.load(file)
        self.api_key = config.get("openai_api_key")
        self.rate_limit = config.get("rate_limit", 60)  # Default to 60 seconds
    
    def get_response(self, prompt: str, model="gpt-4"):
        """Fetch response from OpenAI's API with rate limiting."""
        elapsed_time = time.time() - self.last_request_time
        if elapsed_time < self.rate_limit:
            time.sleep(self.rate_limit - elapsed_time)
        
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": prompt}]
        )
        
        self.last_request_time = time.time()
        return response["choices"][0]["message"]["content"]
    
    def get_market_analysis(self, market_data: dict) -> str:
        """Generate actionable trading insights using real market data"""
        prompt = f"""
        Analyze this Solana market data for trading opportunities:
        {json.dumps(market_data)}
        
        Provide recommendations considering:
        - Recent price movements
        - Liquidity pools
        - Risk management
        """
        
        return self._send_request(prompt)
    
    def get_risk_assessment(self, portfolio: dict) -> str:
        """Generate portfolio risk analysis"""
        prompt = f"""
        Analyze this portfolio risk:
        {json.dumps(portfolio)}
        
        Consider:
        - Asset concentration
        - Market volatility
        - Diversification
        """
        return self._send_request(prompt)