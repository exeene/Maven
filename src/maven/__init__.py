# Import core components
from .core.profile_switcher import ProfileSwitcher
from .core.ai_trader import WaifuTrader

# Expose interface tools
from .interface.character import Character
from .interface.visualizer import Visualizer

# Include integration components
from .llm_integration.openai_client import OpenAIClient
from .llm_integration.persona_engine import PersonaEngine

# Include Solana-related modules
from .solana.client import SolanaClient
from .solana.raydium import Raydium
from .solana.orca import Orca

# Trading components
from .trading.risk_manager import RiskManager
from .trading.strategies import TradingStrategy

# Utility functions
from .utils.configs import load_config
from .utils.helpers import validate_input

# Package version
__version__ = "0.1.0"

# Optional: Define public API
__all__ = [
    'ProfileSwitcher',
    'WaifuTrader',
    'Character',
    'Visualizer',
    'OpenAIClient',
    'PersonaEngine',
    'SolanaClient',
    'Raydium',
    'Orca',
    'RiskManager',
    'TradingStrategy',
    'load_config',
    'validate_input'
]