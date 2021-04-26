# # A class is like an object constructor, or a blueprint for creating objects

# # Python is an object oriented programming language. It's harder to write OOP
# # in python

class AmazingDog:  # Class names should be capitalised w/ no spacing. Snake case

    animal_kind = "canine"  # Variable in class

    def __init__(self, animal_kind):  # Everything that will be initialised upon creation of object
        self.animal_kind = animal_kind
        self.bark()
        self.__is_alive = True  # _is_alive makes it harder to find. __is_alive will stop you from seeing the method at all

    def bark(self):  # Class method
        # print(animal_kind) # # wont work as its not global
        # print(self.animal_kind) # # wont print unless the method is called
        return "woof!"

    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status  # other users should only be able to set methods

    def get_is_alive(self):
        return self.__is_alive


bob = AmazingDog("canine")
# print(dog1.animal_kind)

# dog1.animal_kind = "dolphin"  # Can rename variable if we want
# print(dog1.animal_kind)

sue = AmazingDog("dolphin")  # Create instance of class

# print(bob.__is_alive) # #  wont work as its restricted
# print(bob.get_is_alive())

# might want to hide functionality within classes to make sure that datatypes are correct

# Create a car class. Give the vehicle a maximum speed, and keep track of the current speed of the vehicle.
# It doesn't make sense for the speed to be adjusted directly, so put an underscore in front of it and
# implement a speed getter as well as accelerate and brake setter methods that change the speed in a logical way.
# Do your methods make sense? Does braking past 0 cause the speed to increase?
# Can you accelerate past the car's top speed?


class Car:

    def __init__(self, manufacturer, model, engine_size, number_of_doors, colour, top_speed, speed):
        self.manufacturer = manufacturer
        self.model = model
        self.engine_size = engine_size
        self.number_of_doors = number_of_doors
        self.colour = colour
        self.top_speed = top_speed
        self.speed = speed

    def __repr__(self):
        car_info = f"Name: {self.manufacturer + ',': <10} Type: {self.model + ',': <10} Engine Size: {self.engine_size + ',': <5}\
    Number of Doors: {self.number_of_doors + ',': <6} Colour: {self.colour + ',': <10}\
    Max Speed: {self.top_speed + ',': <7} Current Speed: {self.speed}"
        return car_info

    def get_current_speed(self):
        return self.speed

    def increase_speed(self, value):
        self.speed = float(self.speed) + value
        if self.speed >= float(self.top_speed):
            self.speed = float(self.top_speed)
        return self.speed

    def decrease_speed(self, value):
        self.speed = float(self.speed) - value
        if self.speed <= 0:
            self.speed = 0
        return self.speed


my_car = Car("VW", "Polo", "1.2", "5", "Silver", "100", "0")
print(my_car)
my_car.get_current_speed()
my_car.increase_speed(70)
my_car.decrease_speed(30)
print(my_car)

