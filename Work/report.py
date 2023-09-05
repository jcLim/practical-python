# report.py
#
# Exercise 2.4
from pprint import pprint
import csv
import sys

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price   = float(record['price'])
                total_cost += nshares * price
                portfolio.append(record)
            except ValueError:
                print(f'Row {rowno}: Bad row {row}')
#            holding = (record['shares'], int(record[price]), float(record[2]))

            
        print(total_cost)

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'G:\GettingStarted_Can_Delete\practical-python\Work\Data\portfolio.csv'

out = portfolio_cost(filename)
#print('Portfolio Out:', out)
pprint(out)