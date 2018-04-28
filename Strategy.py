#Strategy pattern

class Animal():
    def __init__(self, name, Sound):
        self.name = name
        self.sound = Sound()

    def make_sound(self):
        print(self.name + " says " + self.sound.get())

class Sound():
    """abstract class"""
    def __inint__(self):
        pass

class DogSound(Sound):
    def get(self):
        return "Woof!"

class CatSound(Sound):
    def get(self):
        return "Meow!"

class BigCatSound(Sound):
    def get(self):
        return "Big MEOW!"


if __name__ == "__main__":

    rex = Animal('dog Rex', DogSound)
    fluffy = Animal('cat Fluffy', CatSound)
    leo = Animal('fat cat Leo', BigCatSound)

    rex.make_sound()
    fluffy.make_sound()
    leo.make_sound()

    #OUTPUT:
    # dog Rex says Woof!
    # cat Fluffy says Meow!
    # fat cat Leo says Big MEOW!
 