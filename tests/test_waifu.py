import pytest
from unittest.mock import Mock, patch
from maven.core.ai_trader import WaifuTrader
from maven.core.profile_switcher import ProfileSwitcher

@pytest.fixture
def mock_solana():
    with patch("maven.solana.client.SolanaClient") as mock:
        mock.return_value.place_order.return_value = "order_123"
        yield mock

@pytest.fixture
def mock_openai():
    with patch("maven.llm_integration.openai_client.OpenAIAPI") as mock:
        mock.return_value.get_response.return_value = "Buy more SOL!"
        yield mock

def test_trade_execution(mock_solana, mock_openai):
    trader = WaifuTrader(base_profile="default")
    result = trader.execute_trade("SOL", 10.0, "buy")
    assert "order_123" in result
    mock_solana.return_value.place_order.assert_called_once()

def test_profile_switching():
    trader = WaifuTrader(base_profile="risk-averse")
    trader.activate_profile("aggressive", 0.2)
    assert trader.profile["risk_tolerance"] == "aggressive"

def test_emotional_support():
    trader = WaifuTrader(base_profile="tsundere")
    msg = trader.provide_emotional_support()
    assert "Stay calm" in msg