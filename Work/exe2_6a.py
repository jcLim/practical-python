import csv

def read_prices(filename):

    out = {}
    f=open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1 :
            out[row[0]] = float(row[1])

    return out

    
