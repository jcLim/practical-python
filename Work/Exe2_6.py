# Execrise 2.6

import csv
from pprint import pprint

def read_prices(filename):
    alist = []
    adict = {}

    f = open('G:\GettingStarted_Can_Delete\practical-python\Work\Data\prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row) == 0 :
            break
        
    #    items = row.split(',')

        print(row)
        adict[row[0]] = float(row[1])
 #       alist.append((adict))
        print(adict)

    f.close
    pprint(adict)
    return adict

# prices = read_prices('G:\GettingStarted_Can_Delete\practical-python\Work\Data\prices.csv')