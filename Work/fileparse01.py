# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_header=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

#    with open(filename) as f:
    headers = []
    indices = []
    records = []
    rows = csv.reader(filename, delimiter=delimiter)

    if select and has_header==False:
        raise RuntimeError('select argument requires column headers')
    else:
        if has_header:
            # Read the file headers
            headers = next(rows)

            # if a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
#            else:
#                indices = []

    for lineno, row in enumerate(rows):
        if not row:
            continue

        try:
            # Types assignment
            if types:
                row = [func(val) for func, val in zip(types, row)]
        except Exception as err:
            if silence_errors==False:
                print('Row %s %s'% (lineno, err))

        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]

        # Make a dictionary
        if has_header:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records

