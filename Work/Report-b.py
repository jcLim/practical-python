# report-b.py
#
# Exercise 2.5

import csv
import sys

def read_portfolio(filename):

    portfolio = {}
    portout = []

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        headers = next(rows)
        print("headers ->",  headers)
        print("headers row - ", headers[0], headers[1], headers[2])

        for line in f:
            row = line.split(',')
            portfolio[headers[0]] = row[0]
            portfolio[headers[1]] = int(row[1])
            portfolio[headers[2]] = float(row[2])
            print(type(portfolio), len(portfolio))

            portout.append(dict(portfolio))
            print(row)
            print(portfolio)
            print(portout)

    return portout


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'G:\GettingStarted_Can_Delete\practical-python\Work\Data\portfolio.csv'

out = read_portfolio(filename)
print('Portfolio Out:', out)