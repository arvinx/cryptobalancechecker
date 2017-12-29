import pprint

from gdax_client import get_balance as get_gdax_balance
from binance_client import get_balance as get_binance_balance

INVESTED = 11000


def merge_balances(b1, b2):
    balances = {}
    for k, v in b1.iteritems():
        if k not in balances:
            balances[k] = v
        else:
            balances[k] += v
    for k, v in b2.iteritems():
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
    gdax = get_gdax_balance()
    binance = get_binance_balance()
    b = merge_balances(gdax, binance)
    total_balance = sum(b.values())
    profit = total_balance - INVESTED

    pp = pprint.PrettyPrinter()
    pp.pprint(pretty_numbers(b))
    print "\nTotal: {}".format('${:,.2f}'.format(total_balance))
    print "Profit: {}".format('${:,.2f}'.format(profit))
