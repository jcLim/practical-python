# report.py
#
# Exercise 2.4
import csv
import sys

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'G:\GettingStarted_Can_Delete\practical-python\Work\Data\portfolio.csv'

out = portfolio_cost(filename)
print('Portfolio Out:', out)