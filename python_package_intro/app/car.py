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