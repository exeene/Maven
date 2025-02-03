import logging
from typing import List

# Configure module-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfileSwitcher:
    def __init__(self, threshold: float = 0.5):
        """
        Initialize the profile switcher with a default volatility threshold.
        :param threshold: A float value representing the volatility threshold.
        """
        self.threshold = threshold

    def calculate_volatility(self, price_history: List[float]) -> float:
        """
        Calculate market volatility based on price history.
        :param price_history: A list of historical prices.
        :return: Calculated volatility as a float.
        """
        if len(price_history) < 2:
            logger.debug("Not enough data to calculate volatility.")
            return 0.0

        price_changes = [
            abs(price_history[i] - price_history[i - 1]) / price_history[i - 1]
            for i in range(1, len(price_history)) if price_history[i - 1] != 0
        ]
        volatility = sum(price_changes) / len(price_changes) if price_changes else 0.0
        logger.debug(f"Calculated volatility: {volatility}")
        return volatility

    def should_switch(self, price_history: List[float], custom_threshold: float = None) -> bool:
        """
        Determine if the AI should switch profiles based on market volatility.
        :param price_history: A list of historical prices.
        :param custom_threshold: Optionally override the default threshold.
        :return: True if volatility meets or exceeds the threshold; otherwise, False.
        """
        threshold = custom_threshold if custom_threshold is not None else self.threshold
        volatility = self.calculate_volatility(price_history)
        should_switch = volatility >= threshold
        logger.debug(f"Volatility {volatility} vs threshold {threshold} => should_switch: {should_switch}")
        return should_switch

    def switch_profile(self, new_profile, volatility_threshold):
        current_volatility = self.trader.get_market_volatility()
        if current_volatility > volatility_threshold:
            self.trader.load_profile(new_profile)