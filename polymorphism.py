# Base class
class Vehicle:
    def move(self):
        # Generic move (can also be abstract in advanced OOP)
        print("Vehicle is moving...")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bike(Vehicle):
    def move(self):
        print("Cycling 🚴")

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()   # Same method name, but each class gives its own behavior
