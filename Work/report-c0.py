import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price
    '''

    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio

ports = read_portfolio('work/data/portfolio.csv')
for row in ports:
 #   print(len(row))
 #   print(row)
 #   print(len(ports[0]))
 #   print(len(row[1]))
 #   print('%1s %10d %10f' % (row['name'], row['shares'], row['price']))
    print('%1s %10d %10f' % (row))