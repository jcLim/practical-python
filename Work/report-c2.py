# pcost.py

import csv

def read_portfolio(filename):
    '''Compute the total cost (shares*price) of a portfolio file'''
    portfolio = []
    holding = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                holding = {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])
                }
                portfolio.append(holding)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return portfolio

def read_prices(filename):
    
    out = {}
    f=open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1 :
            out[row[0]] = float(row[1])

    return out

def make_report(ports, price):
    sval = 0
    cval = 0
    report = []

#    ports = read_portfolio(folioname)
#    price = read_prices(pricename)

    for port in ports:
        stkval = port['shares'] * port['price']
        sval += stkval
        curval = price[port['name']] * port['shares']
        cval += curval
    # **using tuple    
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

portfolio = read_portfolio('work/data/portfolio.csv')
prices = read_prices('work/data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)
# portfolio_report('work/data/portfolio.csv', 'work/data/prices.csv')


