# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, types=None, select=None, has_header=False, delimit=None, silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_header:
        raise RuntimeError ('Select must have has_header selection')

    with open(filename) as f:
        
        # Verify delimiter present
        if delimit:
            rows = csv.reader(f, delimiter=delimit)
        else:
            rows = csv.reader(f)
        
        if has_header:
        # Read the file headers
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows,1):
            if not row:     # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            #if indices:
            #    if types:
            #        row = [fc(row[index]) for fc, index in zip(types, indices)]
            #    else:
            #        row = [row[index] for index in indices]
            #else:
            #    if types:
            #        row = [fc(val) for fc, val in zip(types, row)]

            if indices:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [fc(val) for fc, val in zip(types, row)]
                except ValueError as e:
                    if silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
                



            if has_header:
                # Make a dictionary    
                record = dict(zip(headers, row))
            else:
                # Make tuple
                record = tuple(row)

            records.append(record)

    return records

# Test
# out = parse_csv('work\\data\\portfolio.csv', select=['name','price'], has_header=True, types=[str, float])
# print(out)