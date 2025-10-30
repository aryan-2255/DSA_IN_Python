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
        self.name ="hari"
        self.__atmpin = "2255"
        
