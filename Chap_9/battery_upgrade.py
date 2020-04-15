#!/usr/bin/env python3.7

# JulianV
# Apr 13, 2020.
# Exercise 9-9
# Upgrading electric-car 
# battery adding a new class

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    #Modeling a battery for an electric car.

    def __init__(self, battery_size=60):
        # Initializing battery attributes.
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {str(self.battery_size)}-kWh battery.")

    def get_range(self):
        # Describing range of battery.
        range = 0
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately" + str(range)
        message += " miles on full charge"
        print(message)

    def upgrade_battery(self):
        # Upgrading the battery (*)
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh")
        else:
            print("Battery is already upgrade it.")

class ElectricCar(Car):
    # Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):  
        #Initializing attributes of parent class
        super().__init__(make,model,year)
        #self.battery_size = 70
        self.battery = Battery()

    #lines 40 to 43 can be break into another class
    #def describe_battery(self):
        # Describing battery size
     #   print(f"This car has {str(self.battery_size)}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

my_tesla.battery.upgrade_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()