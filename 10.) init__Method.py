# que

class classplus:
    # attribute
    brand_color = "blue"

    # method_constructor
    def __init__(self):
        print("constructor is called")


pst = classplus()



# que

class Student:
    # Constructor
    def __init__(self):
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




# que 

class Student:
    # Constructor
    def __init__(self, n, r, a, g):
        self.name = n
        self.roll_no = r
        self.age = a
        self.gender = g

    # Method 1
    def display_info(self):   # self refers to the current instance of class
        print(self.name, self.roll_no, self.age, self.gender)


# main
s1 = Student("kp", "4cse042", 23, "male")    # object
s1.display_info()

s2 = Student("nithin", "4cse022", 27, "male")   # object
s2.display_info()
