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

    def key_insert(self):
        print("vechile is started")

    def Break (self):
        print("vechicle is stoped")


# Child class (inherits from Vehicle)
class car(vehicle):
    def start(self,tyre):
        self.tyre = tyre
        print(f"{self.brand} car key inserted, color: {self.color}, tyre count: {tyre}")

# Create object of Car
car_obj = car("toyota","red")

car_obj.start(10)          # from Car class
car_obj.key_insert()     # inherited from Vehicle
car_obj.Break()          # inherited from Vehicle





# 🔹 Types of Inheritance:

# 1️⃣ SINGLE INHERITANCE
# A  →  B
# (One parent → One child)


# 2️⃣ MULTILEVEL INHERITANCE
# A  →  B  →  C
# (Grandparent → Parent → Child)


# 3️⃣ MULTIPLE INHERITANCE
#    A
#    B
#     ↘
#       C
# (One child inherits from two parents)


# 4️⃣ HIERARCHICAL INHERITANCE
#       A
#      / \
#     B   C
# (One parent → multiple children)


# 5️⃣ HYBRID INHERITANCE
#         A
#        / \
#       B   C
#        \ /
#         D
# (Combination of multiple + hierarchical)




# # super

# super is used inside a subclass (child class) to refer to the parent class (also called the superclass).

# | Purpose                         | Python Syntax        | 
# | ------------------------------- | -------------------- | 
# | Call parent constructor         | `super().__init__()` | 
# | Call parent method              | `super().method()`   |
# | Use in inheritance              | ClassName not needed | 
# | Works with multiple inheritance | ✅ Yes                |


class Parent:
    def __init__(self):
        print("Parent constructor called")

    def show(self):
        print("This is the parent method")

class Child(Parent):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        print("Child constructor called")

    def show(self):
        # Call parent version of show()
        super().show()
        print("This is the child method")

# Create object
obj = Child()
obj.show()




# multi level inheritance

class Grandparent:
    def show_grandparent(self):
        print("I am the Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am the Parent")

class Child(Parent):
    def show_child(self):
        print("I am the Child")

# Create object of the Child class
obj = Child()

obj.show_grandparent()  # inherited from Grandparent
obj.show_parent()       # inherited from Parent
obj.show_child()        # defined in Child

