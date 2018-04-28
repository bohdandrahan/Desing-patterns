#Composite design 


class Component():

    def get_price(self):
        return self.price
    def add_item(self, item):
        pass
    def remove_item(self, item):
        pass

class Composite(Component):

    def __init__(self):
        self.items = list()

    def get_price(self):
        self.price = 0
        for item in self.items:
            self.price += item.get_price()
        return self.price

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Leaf(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)


a = Leaf('a', 1)
b = Leaf('b', 2)

c = Composite()

c.add_item(a)
c.add_item(b)


print(c.get_price())



