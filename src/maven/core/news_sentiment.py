import openai

class NewsSentimentAnalyzer:
    """Analyzes the sentiment of news articles using OpenAI's GPT."""
    
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_sentiment(self, news_article):
        """Analyzes sentiment of the provided news article text."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[{"role": "system", "content": "Analyze the sentiment of the following news article."},
                          {"role": "user", "content": news_article}]
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error analyzing sentiment: {e}"
