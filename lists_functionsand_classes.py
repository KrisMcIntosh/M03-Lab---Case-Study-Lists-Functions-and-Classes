# M03 Lab - Lists, Functions, and Classes
# author: Kris McIntosh
# created: 2022-02-01  updated: 2022-02-01 (Kris McIntosh)
# A program to list vehicles.

# List
car = Automobile(2022, "Toyota", "Corolla", 4, "sun roof")

# Create the Vehicle class
class Vehicle:
    def __init__(self, type):
        self.type = type

# Create the Automobile class
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        Vehicle.__init__(self, "Automobile")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Print the output
print("Vehicle type:", car.type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)