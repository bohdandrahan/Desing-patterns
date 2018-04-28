#Composite design 


class Component():
    #Abstract class
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def print_price(self):
        print("Price of " + str(self.get_name()) + ": " + str(self.get_price()))


class Composite(Component):

    def __init__(self, name):
        self.name = name
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

if __name__ == "__main__":

    simple_part1 = Leaf('simple_part1', 1)
    simple_part2 = Leaf('simple_part2', 2)
    
    complex_part = Composite('complex_part')
    
    complex_part.add_item(simple_part1)
    complex_part.add_item(simple_part2)
    
    simple_part1.print_price()
    simple_part2.print_price()
    complex_part.print_price()

    #Output:
    # Price of simple_part1: 1.0
    # Price of simple_part2: 2.0
    # Price of complex_part: 3.0
