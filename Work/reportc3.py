# reportc3.py for Exe 4.4

import csv
import gzip
import stock
from fileparse01 import parse_csv

def make_report(ports, price):
    sval = 0
    cval = 0
    curval = 0
    report = []

    for port in ports:
        stkval = port.cost()
        sval += stkval

        skey = port.name
        rid = 0
        for idx, key in enumerate(price):
            if key[0] == skey:
                rid == idx
                break

        curval = price[idx][1] * port.shares
        cval += curval
    # **using tuple    e
        lineval = (
            port.name,
            port.shares,
            port.price,
            float(curval - stkval)
        )
        report.append(lineval)

    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' %headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
    # **using tuple
        print('%10s %10d $%9.2f %10.2f' % row)

    return

def read_portfolio(portfile, pricefile):
    with open(portfile, 'rt') as pf1:
        portdicts = parse_csv(pf1, select=['name','shares','price'], types=[str, int, float])
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

    with open(pricefile, 'r') as pf2:
        prices = parse_csv(pf2, types=[str, float], has_header=False)

    report = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    read_portfolio(args[1], args[2])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
