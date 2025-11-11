#  What is Abstraction?

# Abstraction means hiding the complex details and showing only the necessary features.

# In simple words — you don’t need to know how something works internally, just how to use it.

# For example:
# When you drive a car 🚗, you just use the steering, brake, and accelerator —
# you don’t need to know how the engine works inside.

# In Python, we achieve abstraction using the abc module (Abstract Base Class).


# 🧩 Rules of Abstraction

# Use from abc import ABC, abstractmethod

# Create a class that inherits from ABC

# Use the @abstractmethod decorator for methods that must be overridden

# You cannot create an object of an abstract class directly



# # ex

# abstraction.py

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Concrete class 1
class Car(Vehicle):
    def start(self):
        print("Car engine started with a key 🔑")

    def stop(self):
        print("Car engine stopped.")


# Concrete class 2
class Bike(Vehicle):
    def start(self):
        print("Bike started with a self-start button ⚙️")

    def stop(self):
        print("Bike engine turned off.")


# Main code
car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()




# # ex 


from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self, c):
        self.color = c

    @abstractmethod
    def area(self):
        pass

    def display_color(self):
        pass


class circle(shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
       print(f" area of circle id {3.14*self.radius**2}")


class rectangle(shape):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        print(f"area of rectangle is {self.length*self.breadth}")


co = circle(10)
co.area()


