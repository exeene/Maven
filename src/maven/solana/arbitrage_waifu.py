from .client import SolanaClient

class ArbitrageWaifu:
    def __init__(self, client: SolanaClient):
        self.client = client

    def find_arbitrage_opportunities(self):
        prices = self.client.get_prices()
        opportunities = []
        for pair in prices:
            if prices[pair]['raydium'] > prices[pair]['orca']:
                opportunities.append({
                    'pair': pair,
                    'buy_from': 'orca',
                    'sell_to': 'raydium',
                    'profit': prices[pair]['raydium'] - prices[pair]['orca']
                })
        return opportunities