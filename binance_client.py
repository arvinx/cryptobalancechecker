from binance.client import Client
from coinmarketcap_client import get_coin_price

from keys import binance_key, binance_secret

client = Client(binance_key, binance_secret)


def get_balance():
    """
    Get mapping from coin to balance in USD
    """
    balances = {}
    accounts = client.get_account()['balances']
    for account in accounts:
        if float(account['free']) > 0:
            price = get_coin_price(account['asset'])
            balances[str(account['asset'])] = price * float(account['free'])
    return balances

