# class and object

# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.





class student:
    #attributes
    roll_no = 0
    name = ""
    age = ""
    gender = ""


s1 = student() #object
s1.name = "hari"
s1.roll_no = 78

s2 = student() #object
s2.name = "aryan"


print(s1.roll_no)
print(s2.name)




class student:
    #attributes
    roll_no = 0
    name = ""
    age = ""
    gender = ""

    def display_info(self):           # self- referces current instance of class
     print(self.name,self.roll_no)


s1 = student() #object
s1.name = "hari"
s1.roll_no = 78

s2 = student() #object
s2.name = "aryan"


print(s1.roll_no)
print(s2.name)




class student:
    #attributes
    roll_no =0
    name=""
    age=""
    gender=""
    #method 1
    #self refers to the current instance of the class
    def display_info(self):
        print(self.name, self.roll_no, self.age, self.gender)
    #method 2
    def set_info(self):
        self.name = input("Enter the student name")
        self.roll_no = input("Enter the Roll Number")
        self.age = input("Enter the Age")
        self.gender = input("Enter the gender")

s1 = student()

s1.set_info()
s1.display_info()