import pytest
import json
from maven.core.ai_trader import WaifuTrader

def test_custom_profile_loading(tmp_path):
    custom_profile = tmp_path / "custom.json"
    custom_profile.write_text(json.dumps({
        "name": "TestChan",
        "risk_tolerance": "moderate"
    }))
    
    trader = WaifuTrader(base_profile=str(custom_profile))
    assert trader.profile["name"] == "TestChan"
    assert trader.risk_manager.tolerance == "moderate"

def test_default_profile():
    trader = WaifuTrader(base_profile="default")
    assert "risk_tolerance" in trader.profile
    assert "personality" in trader.profile