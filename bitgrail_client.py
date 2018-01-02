import hmac
import hashlib
from time import time

import requests
from coinmarketcap_client import get_coin_price
from keys import bitgrail_key, bitgrail_secret

BALANCE_API = 'https://bitgrail.com/api/v1/balances'

def get_balance():
    """
    Get mapping from coin to balance in USD
    """
    balances = {}
    accounts = bitgrail_get_accounts()
    for currency in accounts.keys():
        balance = float(accounts[currency]['balance'])
        if balance > 0:
            price = get_coin_price(currency)
            balances[str(currency)] = price * balance
    return balances

def bitgrail_get_accounts():
    # Nonce is time past epoch in nanos
    data = 'nonce={}'.format(int(time() * 1e9)).encode('utf-8')
    signature = hmac.new(bitgrail_secret.encode('utf-8'), data, hashlib.sha512).hexdigest()
    headers = {
        'KEY': bitgrail_key,
        'SIGNATURE': signature,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return requests.post(BALANCE_API, headers=headers, data=data).json()['response']
