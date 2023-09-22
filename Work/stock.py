# Define stock class

class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price        

    @property
    def cost(self):
        return self.price * self.shares
        
    def sell(self, sold):
        self.shares -= sold

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected  int')
        self._shares = value


class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return 1.25 * self.price * self.shares


