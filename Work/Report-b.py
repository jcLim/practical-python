# report-b.py
#
# Exercise 2.5

import csv
import sys

def read_portfolio(filename):

    portfolio = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in f:
            portfolio[headers[0]] = row[0]
            portfolio[headers[1]] = row[1]
            portfolio[headers[2]] = row[2]
 #           holding = (row[0], int(row[1]), float(row[2]))
 #           portfolio.append(holding)

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'G:\GettingStarted_Can_Delete\practical-python\Work\Data\portfolio.csv'

out = read_portfolio(filename)
print('Portfolio Out:', out)