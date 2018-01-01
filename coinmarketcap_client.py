import requests

endpoint = "https://api.coinmarketcap.com/v1/ticker/"

ticker_to_name = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'LTC': 'litecoin',
    'STRAT': 'stratis',
    'IOTA': 'iota',
    'ZEC': 'zcash',
    'DASH': 'dash',
    'XRP': 'ripple',
    'ADA': 'cardano',
    'XLM': 'stellar',
    'NEO': 'neo'
}


def get_coin_price(ticker):
    name = ticker_to_name[ticker]
    r = requests.get(endpoint + name)
    return float(r.json()[0]['price_usd'])
