# Expose core functionality
from .waifu import AIWaifu
from .character import Character
from .strategy import TradingStrategy
from .api import OpenAIAPI

__all__ = ['AIWaifu', 'Character', 'TradingStrategy', 'OpenAIAPI']