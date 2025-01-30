import pytest
from maven.core.profile_switcher import ProfileSwitcher

def test_volatility_calculation():
    ps = ProfileSwitcher()
    prices = [100, 105, 98, 110, 95]
    volatility = ps.calculate_volatility(prices)
    assert 0.05 < volatility < 0.15

def test_profile_switch_decision():
    ps = ProfileSwitcher(threshold=0.1)
    stable_prices = [100, 101, 100, 102]
    volatile_prices = [100, 115, 90, 120]
    
    assert not ps.should_switch(stable_prices)
    assert ps.should_switch(volatile_prices)