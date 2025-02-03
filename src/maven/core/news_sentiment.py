import openai

class NewsSentimentAnalyzer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_sentiment(self, news_article):
        response = openai.GPT4.analyze(news_article)
        return response.sentiment