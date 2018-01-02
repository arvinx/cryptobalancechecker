import pprint

from gdax_client import get_balance as get_gdax_balance
from binance_client import get_balance as get_binance_balance
from bitgrail_client import get_balance as get_bitgrail_balance
from keys import INVESTED, USE_GDAX, USE_BINANCE, USE_BITGRAIL


def merge_balances(input_balances):
    balances = {}
    for input_balance in input_balances:
        for k, v in input_balance.iteritems():
            if k not in balances:
                balances[k] = v
            else:
                balances[k] += v
    return balances


def pretty_numbers(b):
    for k, v in b.iteritems():
        b[k] = '${:,.2f}'.format(b[k])
    return b


if __name__=='__main__':
    accounts = []
    if USE_GDAX:
        accounts.append(get_gdax_balance())
    if USE_BINANCE:
        accounts.append(get_binance_balance())
    if USE_BITGRAIL:
        accounts.append(get_bitgrail_balance())
    b = merge_balances(accounts)
    total_balance = sum(b.values())
    profit = total_balance - INVESTED

    pp = pprint.PrettyPrinter()
    pp.pprint(pretty_numbers(b))
    print "\nTotal: {}".format('${:,.2f}'.format(total_balance))
    print "Profit: {}".format('${:,.2f}'.format(profit))
