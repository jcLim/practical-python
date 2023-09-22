# pcost.py

import csv
import gzip
from fileparse01 import parse_csv

#def read_portfolio(filename):
#   '''Compute the total cost (shares*price) of a portfolio file'''
#    portfolio = []
#    holding = {}
#
#    with open(filename, 'rt') as f:
#        rows = csv.reader(f)
#        headers = next(rows)
#        for rowno, row in enumerate(rows, start=1):
#            record = dict(zip(headers, row))
#            try:
#                holding = {
#                    'name': record['name'],
#                    'shares': int(record['shares']),
#                    'price': float(record['price'])
#                }
#                portfolio.append(holding)
#            except ValueError:
#                print(f'Row {rowno}: Bad row: {row}')
#
#    return portfolio
#
#
#def read_prices(filename):
#    
#    out = {}
#    f=open(filename, 'r')
#    rows = csv.reader(f)
#    for row in rows:
#        if len(row)>1 :
#            out[row[0]] = float(row[1])
#
#    return out

def make_report(ports, price):
    sval = 0
    cval = 0
    curval = 0
    report = []

#    ports = read_portfolio(folioname)
#    price = read_prices(pricename)
    for port in ports:
        stkval = port['shares'] * port['price']
        sval += stkval

        skey = port['name']
        rid = 0
        for idx, key in enumerate(price):
            if key[0] == skey:
                rid == idx
                break

        curval = price[idx][1] * port['shares']
        cval += curval
    # **using tuple    e
        lineval = (
            port['name'],
            port['shares'],
            port['price'],
            float(curval - stkval)
        )

    # **using dict
    #    lineval = {
    #        'name': port['name'],
    #        'shares': port['shares'],
    #        'price': port['price'],
    #        'change': float(curval - stkval)
    #   }
        report.append(lineval)

    return report

def print_report(report):

#    report=cal_curr_price(folio_file, price_file)
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' %headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
    # **using tuple
        print('%10s %10d $%9.2f %10.2f' % row)

    # **using dict
    #    print('%10s %10d %10.2f %10.2f' % 
#          (row['name'], row['shares'], row['price'], row['change']))
    return

def pf_report(portfile, pricefile):
#    portfolio = parse_csv(portfile, select=['name','shares','price'], types=[str, int, float])
#    prices = parse_csv(pricefile, types=[str, float], has_header=False)

    with open(portfile, 'rt') as pf1:
        portfolio = parse_csv(pf1, select=['name','shares','price'], types=[str, int, float])

    with open(pricefile, 'r') as pf2:
        prices = parse_csv(pf2, types=[str, float], has_header=False)

    report = make_report(portfolio, prices)
    print_report(report)
    # portfolio_report('work/data/portfolio.csv', 'work/data/prices.csv')

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    pf_report(args[1], args[2])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
