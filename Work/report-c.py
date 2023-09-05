# pcost.py

import csv

def read_portfolio(filename):
    '''Compute the total cost (shares*price) of a portfolio file'''
    portfolio = []
    holding = {}


    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                headers[0]: (row[0]),
                headers[1]: int(row[1]),
                headers[2]: float(row[2])
            }
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    
    out = {}
    f=open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1 :
            out[row[0]] = float(row[1])

    return out

sval = 0
cval = 0

ports = read_portfolio('work/data/portfolio.csv')
print(ports)
price = read_prices('work/data/prices.csv')
for port in ports:
    stkval = port['shares'] * port['price']
    sval += stkval
    curval = price[port['name']] * port['shares']
    cval += curval
    print(port['name'], port['shares'], port['price'], stkval, curval)
    print(sval, cval)

# print(portfolio_cost('work/data/portfolio.csv'))