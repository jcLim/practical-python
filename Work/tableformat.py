# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CVSTableFormatter(TableFormatter):
    '''
    Output portfolio data in CVS format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print('<th>', f'{h:s}','</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>', f'{d:s}', '</td>', end=' ')
        print('</tr>')

class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == 'txt':
        return TableFormatter()
    elif fmt == 'cvs':
        return CVSTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % fmt)
    
def print_table(file, columns, formatter):
    formatter.headings(columns)

    for data in file:
        dataout = []
        for col in columns:
            dataout.append(str(getattr(data, col)))
        formatter.row(dataout)

