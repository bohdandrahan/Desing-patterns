#Decorator pattern

class Animal():
   #component 
    """Abstract class"""
    def __init__(self, name):
        self.name = name
    def sound(self):
        #abstract method
        pass
    def does_fly(self):
        #abstract method
        pass
    def get_name(self):
        return self.name


class Horse(Animal):
    #Concrete component
    def sound(self):
        return str( "My name is " + self.name +". I am like a Horse")

    def does_fly(self):
        return False

class Decorator(Animal):
    def __init__(self, animal):
        self.animal = animal
        self.name = animal.get_name()

    def sound(self):
        return self.animal.sound()

    def does_fly(self):
        return self.animal.does_fly()

class LongNecker(Decorator):
    #Concrete decorator
    def sound(self):
        return str(self.animal.sound() + '. But I also has a long neck')

class HasWingser(Decorator):
    #Concrete decorator
    def sound(self):
        return str(self.animal.sound() + '. But I also has a pair of wings')

    def does_fly(self):
        return True

class HasHorner(Decorator):
    #Concrete decorator
    def sound(self):
        return str(self.animal.sound() + '. But I also has a horn')

if __name__ == "__main__":

    horse = Horse("Horse Ace")
    giraffe = LongNecker(Horse("Giraffe LooLoo"))
    pegasus = HasWingser(Horse("Pegasus Peggy"))
    unicorn = HasHorner(Horse("Unicorn Rainbowie"))
    unicorn_giraffe = HasHorner(LongNecker(Horse("Unicron Giraffe Leonid")))


    print(horse.sound())
    print(giraffe.sound())
    print(pegasus.sound())
    print(unicorn.sound())
    print(unicorn_giraffe.sound())

    #OUTPUT:
    # My name is Horse Ace. I am like a Horse
    # My name is Giraffe LooLoo. I am like a Horse. But I also has a long neck
    # My name is Pegasus Peggy. I am like a Horse. But I also has a pair of wings
    # My name is Unicorn Rainbowie. I am like a Horse. But I also has a horn
    # My name is Unicron Giraffe Leonid. I am like a Horse. But I also has a long neck. But I also has a horn