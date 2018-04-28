#Strategy pattern

class Animal():
    def __init__(self, name, Sound):
        self.name = name
        self.sound = Sound()

    def make_sound(self):
        print(self.sound.get())

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


rex = Animal('dog Rex', DogSound)
mike = Animal('cat Mike', CatSound)
leo = Animal('fat cat Leo', BigCatSound)

rex.make_sound()
mike.make_sound()
leo.make_sound()

