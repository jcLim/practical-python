# Exe2_7


import csv
import os


def read_portfolio(filename):
    
    portout = []
    total_cost = 0.0

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        headers = next(rows)

        for rowno, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try:
                nshares = int(record['shares'])
                price   = float(record['price'])
                total_cost += nshares * price
                portout.append((record))
            except ValueError:
                print(f'Row {rowno}: Bad row: {line}')

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

def make_report(portfolio, prices):

    rpt = []
    out = portfolio
    changes = 0.0

#print(prices)


    for line in out:
    #    print(line['name'])
        t = line['name']
        ts = t.strip('""')
        changes = prices[ts] - float(line['price']) 
        holding = (ts, int(line['shares']), prices[ts], changes)
        rpt.append(holding)

    return rpt


#print(f'{"Name" : >10} {"Shares" : >10} {"Price" : >10} {"Changes" : >10}' )
#print(f"{ts : >10} {line['shares'] : >10.0f} {line['price'] : >10.2f} {changes : >10.2f}")


# print(netvalue)
out     = read_portfolio('Data\\portfolio.csv')
#print(out)
prices  = read_prices('Data\\prices.csv')
#print(prices)
report  = make_report(out, prices)
#print(report)

#print(f'{"Name" : >10} {"Shares" : >10} {"Price" : >10} {"Changes" : >10}' )
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]: >10} {headers[1]: >10} {headers[2]: >10} {headers[3]: >10}')
print(f"{'-'*10: >10} {'-'*10: >10} {'-'*10: >10} {'-'*10: >10}")

for name, shares, price, changes in report:
#        print(r)
        pricefmt = "${:.2f}".format(price)
        print(f"{name : >10} {shares : >10.0f}  {pricefmt : >9}  {changes : >10.2f}")



#total_cost = 0.0
#for s in out:
#    total_cost += s['shares']*s['price']

#print('Total cost', total_cost)

# Compute the current value of the out
#total_value = 0.0
#for s in out:
#    t = s['name']
#    ts = t.strip('""')
#    total_value += s['shares']*prices[ts]

#print('Current value', total_value)
#print('Gain', total_value - total_cost)
