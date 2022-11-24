# Exe2_7


import csv
import os


def read_portfolio(filename):
    
    portout = []

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        headers = next(rows)

        for line in f:
            row = line.split(',')
            out = {
                    headers[0]  : row[0], 
                    headers[1]  : int(row[1]),
                    headers[2]  : float(row[2])
                        }
            portout.append((out))

    return portout



def read_prices(filename):
    alist = []
    adict = {}

    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row) == 0 :
            break
        adict[row[0]] = float(row[1])

    f.close
    return adict

netvalue = 0.0
out     = read_portfolio('.\\.\\Work/Data/portfolio.csv')
prices  = read_prices('.\\.\\Work/Data/prices.csv')

#print(prices)

for line in out:
#    print(line['name'])
    t = line['name']
    ts = t.strip('""')
    print(t, type(t), ts)
    print(prices.get(ts))
#    print(line['name'], shares, price)
#    print(line[1], line[0], line[2])
#   print(prices[line[0]])
#    netvalue += (line['shares'] * prices[ts]) - (line['shares'] * line['price'])


# print(netvalue)

total_cost = 0.0
for s in out:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the out
total_value = 0.0
for s in out:
    t = s['name']
    ts = t.strip('""')
    total_value += s['shares']*prices[ts]

print('Current value', total_value)
print('Gain', total_value - total_cost)
