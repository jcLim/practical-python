# reportc4.py for Exe 4.5

import csv
import gzip
import stock
import tableformat
from fileparse01 import parse_csv

def make_report_data(ports, price):
    sval = 0
    cval = 0
    curval = 0
    report = []

    for port in ports:
        stkval = port.cost
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

def print_report(report, formatter):
    headers = ('Name', 'Shares', 'Price', 'Change')
#    headers = columns   
    formatter.headings(headers)
#    print('%10s %10s %10s %10s' %headers)
#    print(('-' * 10 + ' ') * len(headers))
    for row in report:
    # **using tuple
        rowout = [f'{row[0]:s}', f'{row[1]:d}', f'${row[2]:0.2f}', f'{row[3]:0.2f}']
        formatter.row(rowout)
#        print('%10s %10d $%9.2f %10.2f' % row)
    return

def read_portfolio(portfile):
    with open(portfile, 'rt') as pf1:
        portdicts = parse_csv(pf1, select=['name','shares','price'], types=[str, int, float])
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(pricefile):
    with open(pricefile, 'r') as pf2:
        prices = parse_csv(pf2, types=[str, float], has_header=False)
    return prices

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolio, prices)

#    formatter = tableformat.TableFormatter()
#    formatter = tableformat.CVSTableFormatter()
#    formatter = tableformat.HTMLTableFormatter()
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile fmt' % args[0])
    portfolio_report(args[1], args[2], args[3])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
