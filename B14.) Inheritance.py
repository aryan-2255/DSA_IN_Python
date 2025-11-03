# # INHERITANCE – SHORT NOTES

# 🔹 Definition:
# Inheritance is an object-oriented programming (OOP) concept in which a child class acquires the properties and methods of a parent class. 
# It allows code reusability and helps to build a relationship between classes.

# 🔹 Key Points:
# 1. The parent class (superclass) provides common features.
# 2. The child class (subclass) inherits those features and can add or modify them.
# 3. It helps to reduce code duplication and improve maintainability.
# 4. Supports polymorphism and hierarchical organization in OOP.

# 🔹 Advantages:
# - Promotes code reusability.
# - Makes programs easier to maintain and extend.
# - Supports method overriding and polymorphism.
# - Reduces redundancy of code.

# 🔹 Types of Inheritance:
# 1. Single Inheritance – One child inherits one parent.
# 2. Multilevel Inheritance – Chain of inheritance (A → B → C).
# 3. Multiple Inheritance – A class inherits from more than one parent (Python supports this).
# 4. Hierarchical Inheritance – Multiple children inherit from one parent.
# 5. Hybrid Inheritance – Combination of above types.

# 🔹 Example (Conceptual):
# Parent Class: Animal → has method eat()
# Child Class:  Dog → inherits eat(), adds bark()

# 🔹 Summary:
# Parent / Superclass → Base class whose properties are inherited
# Child / Subclass → Derived class that inherits from parent
# Main Benefit → Code reusability & extensibility
# Keyword → 'extends' (JavaScript/Java), ':' (Python)



# 🔹 syntax:

# class Parent {
#     // parent properties and methods
# }

# class Child extends Parent {
#     // additional or modified properties and methods
# }



# # ex

class vehicle():

    def __init__(self, b, c):
        self.brand = b
        self.color = c

    def start (self):
        print("vechile is started")

    def Break (self):
        print("vichle is started")

    class car(vehicle):
        pass
    car_obj = car("toyota","red")
    car_obj.key_insert()