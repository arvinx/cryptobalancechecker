import gdax
from keys import gdax_key, gdax_b64secret, gdax_passphrase

public_client = gdax.PublicClient()
auth_client = gdax.AuthenticatedClient(gdax_key, gdax_b64secret, gdax_passphrase)


gdax_products = ['BTC', 'ETH', 'LTC']


def get_balance():
    """
    Get mapping from coin to balance in USD
    """
    balances = {product: 0 for product in gdax_products}
    accounts = auth_client.get_accounts()
    prices = {product: public_client.get_product_ticker(product_id="{}-USD".format(product))['price']
              for product in gdax_products}
    for account in accounts:
        if account['currency'] in balances:
            balances[str(account['currency'])] = float(account['balance']) * float(prices[account['currency']])
    return balances

