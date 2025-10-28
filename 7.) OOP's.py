# class and object

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