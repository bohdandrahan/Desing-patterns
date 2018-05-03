#Abstract Factory


class Transport():
    #Abstract factory
    def get_model(self):
        return self.model

    def get_speed(self):
        return self.speed

    def get_number_of_seats(self):
        return self.number_of_seats

    def get_horsepower(self):
        return self.horsepower

class Horse(Transport):
    #Concrete factory
    def __init__(self, name):
        self.name = name
        self.speed = '30 mph'
        self.number_of_seats = '2-ish'
        self.horsepower = 1  

    def get_model(self):
        return "Horse " + str(self.name)

class Car(Transport):
    #Concrete factory
    def __init__(self, model):
        self.model = model
        self.speed = '65 mph'
        self.number_of_seats = 5
        self.horsepower = 300

class AirPlane(Transport):
    #Concrete factory
    def __init__(self, model):
        self.model = model
        self.speed = '500 mph'
        self.number_of_seats = 250
        self.horsepower = 95710 


def move_client(transport):
    print('moving form A to B')

    print('Vehicle: ' + transport.get_model())

    print("Speed: " + transport.get_speed())

    print("Number of seats: " + str(transport.get_number_of_seats()))

    print("Horsepower: " + str(transport.get_horsepower()))
    print('\n')



if __name__ == '__main__':

    horse = Horse('Jupiter')
    car = Car('Honda Accord 2018')
    airplane = AirPlane('Boeing 747')

    move_client(horse)
    move_client(car)
    move_client(airplane)

    #Output:
    # moving form A to B
    # Vehicle: Horse Jupiter
    # Speed: 30 mph
    # Number of seats: 2-ish
    # Horsepower: 1


    # moving form A to B
    # Vehicle: Honda Accord 2018
    # Speed: 65 mph
    # Number of seats: 5
    # Horsepower: 300


    # moving form A to B
    # Vehicle: Boeing 747
    # Speed: 500 mph
    # Number of seats: 250
    # Horsepower: 95710

  


