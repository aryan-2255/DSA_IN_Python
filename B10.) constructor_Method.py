# question

class classplus:
    # attribute
    brand_color = "blue"

    # method_constructor
    def __init__(self):
        print("constructor is called")


pst = classplus()




# question

class Student:
    # Constructor
    def __init__(self):             # default constructor-  only self we use
        self.name = input("Enter the name: ")
        self.roll_no = input("Enter the roll number: ")
        self.age = int(input("Enter the age: "))
        self.gender = input("Enter the gender: ")

    # Method 1
    def display_info(self):   # self refers to current instance (object)
        print(self.name, self.roll_no, self.age, self.gender)


# main
s1 = Student()    # Object created — constructor runs automatically
s1.display_info() # Display info




# question

class Student:
    # Constructor
    def __init__(self, n, r, a, g):    # paramatrized constructor - we use other paraameters with self then define it below
        self.name = n
        self.roll_no = r
        self.age = a
        self.gender = g

    # Method 1
    def display_info(self):   # self refers to the current instance of class
        print(self.name, self.roll_no, self.age, self.gender)


# main

s1 = Student("kp", "4cse042", 23, "male") 
s1.display_info()

s2 = Student("nithin", "4cse022", 27, "male")   # object
s2.display_info()






# question

class lessnumerror(Exception):
    pass
class morenumerror(Exception):
    pass
n = int(input("enter the number"))
try:
    if(n<0):
        raise lessnumerror("less number error")
    elif(n>10):
        raise morenumerror("moer number error")
except lessnumerror as msg:
    print(msg)
except morenumerror as msg:
    print(msg)
else:
    print(n)


# question

class laptop:
    def   __init__(self,b,p):
        self.brand = b
        self.price = p
    def turn_on(self):
        print(f"{self.brand}laptop is on")
    def display_info(self):
        print(f"brand is {self.brand} price is {self.price}")

obj1= laptop("hp", 50000)
obj1.turn_on
obj1.display_info

# 

class Laptop:
    def __init__(self, brand, price):    # constructor
        print(f"{brand} is the laptop brand and the price is {price}")
        print(f"{brand} Laptop is now ON!")

# creating objects
Laptop("apple", 10000)
Laptop("hp", 100)



class employee:
    def __init__(self,n,s,d):
        self.name =  n
        self.salary = s
        self.department = d
    def bonuse(self):
        if(self.department == "sales"):
            self.salary += self.salary*0.1
        else:
            self.salary += self.salary*0.5
    def get_salary(self):
        print(self.salary)


emp1 = employee("ridhi",200,"sales")
emp1.bonus()
emp1.get_salary()
emp2 = employee("varad", 350,"thakadar")
emp2.bonus()
emp2.get_salary()


# question

class calculator:

    def addition(self,a,b):
        print(a+b)
    def subtraction(self,a,b):
        print(b-a)
    def multiplication(self,a,b):
        print(a*b)
    def division(self,a,b):
        print(a/b)

c1 = calculator()
c1.addition(10,20)
c1.subtraction(10,20)
c1.multiplication(10,20)
c1.division(20,10)