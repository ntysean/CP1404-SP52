

class Car:
    def __init__(self, name = "", fuel=0):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def drive2(self, distance):
        if distance>self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self.odometer += distance
        return distance_driven

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)
















