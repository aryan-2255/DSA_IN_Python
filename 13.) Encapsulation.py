# Encapsulation means -
# “wrapping data and methods together into a single unit (class)”
# and restricting direct access to some parts of an object.


# 👉 Think of it as putting all your important data in a capsule (class) and locking it,
# so no one can directly touch it — they can only use it through methods you allow.


# | Concept           | Example                                                       |
# | ----------------- | ------------------------------------------------------------- |
# | Encapsulation     | Hiding data and providing access through methods              |
# | Achieved by       | Using private variables (`__var`) and public methods          |
# | Real life example | ATM — you can withdraw but not change your bank data directly |


# | Type          | Symbol       | Access Level                               |
# | ------------- | ------------ | ------------------------------------------ |
# | **Public**    | `variable`   | Accessible **from anywhere**               |
# | **Protected** | `_variable`  | Accessible **within class and subclasses** |
# | **Private**   | `__variable` | Accessible **only inside the class**       |





# ex

class person:
    def __init__(self):
        # public attribute
        self.name ="hari"

        # private attribute
        self.__atmpin = "2255"

      # public mehod
    def print_info(self):
        print("information about person")
       # private method
    def __display_info(self):
        print("display info about person")

       # getter function 
    def get_atmpin(self):
        print(self.__atmpin)
        # setter function
    def set_atmpin(self, new_pin):
         self.__atmpin = new_pin



p1 = person()
p1.print_info()                   # ✅ works
print(p1.name)                    # ✅ works

# print(p1.__atmpin)              # ❌ error
# p1.__display_info()             # ❌ error

p1.set_atmpin(9876)   # update the private attribte
p1.get_atmpin()       # accessed the private attribute

