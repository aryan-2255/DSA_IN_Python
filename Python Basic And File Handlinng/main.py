print("hello aryan choudhary!")

print(" aryan \n choudhary!")
# here \n is for seperating the text

print("i am from haryana", end ='\n')
print("i am from narnaul")
# here end ='\n' is use for seperating too after that new line start in different line


# solution -1
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")

# solution -2
print("*\n**\n***\n****")
# there is a simple funda how much short code you write easy to handle it also same as before but in short version

# question
print("MENU")
print("tea    rs.10")
print("coffee rs.20")
print("juice  rs.30")
# solution -1
print("""
      MENU
      tea       rs.10
      coffee    rs.20
      juice     rs.30
      papaya    rs.40
      """)
# solution -2
print("menu\n tea\t rs.10 \n coffee\t rs.20 \n juice\t rs.30" )
# here \t is for giving 4 space between

# question
# solution-1
print("\t *")
print("\t***")
print("      ******")
print("\t***")
print("\t *")
# solution 2
print("\t * \n \t*** \n       ****** \n \t*** \n \t * ")

# question for a triangle
# solution -1

''' 
what is variable?
container to store data
data types?
  integer:
          whole no.
          natural no.
          negative no.

  float:
        real no.
        rational no.
  char:
       'a','b','c','@','{}','-'
  boolean:
          true and false

'''
x = 2
y = 3
sum = x + y
print(sum)
 
a = 5
b = 10
sum = a + b
print("the sum of above two number is:",a+b,sum)
print(type(a+b))

'''
naming variable

2name = "Aryan"    # starts with digit
user-name = 100    # hyphen not allowed
for = 5            # keyword

1. Variable Naming Rules

Letters, digits, aur underscore allowed

Valid: age, user_name, score2

Invalid: 2score (digit se start nahi ho sakta), user-name (hyphen not allowed)

Cannot start with a digit

age1 = 25    # ✅ valid
1age = 25    # ❌ invalid


Case-sensitive

age, Age, AGE → ye 3 alag variables hain.

Cannot use keywords

Python keywords jaise if, for, while, class variable names nahi ho sakte.

Underscores allowed

Single underscore: _temp

Double underscore (special meaning in classes): __init__
'''
'''
1. snake_case	user_name, total_score	Words lowercase, separated by _. Python standard for variables & functions.

2. camelCase	userName, totalScore	First word lowercase, next words start with uppercase. Common in JavaScript & Java variables/functions.

3. PascalCase	UserName, TotalScore	First letter of all words uppercase. Common for Class names in many     languages.

4. kebab-case	user-name, total-score	Words lowercase, separated by -. Mostly used in URLs or CSS class names.

5. UPPERCASE_SNAKE_CASE	MAX_SCORE, PI_VALUE	All uppercase, words separated by _. Usually constants.

'''

age = 25
print(age)

x = 100
y = 100
z = 100
print(x,y,z)
x,y,z = 100,100,100
print(x,y,z)
x = y = z = 100
print(x,y,z)

'''

1. string: "delhi" A string is a sequence of characters (letters, numbers, symbols).
                   In Python, strings are enclosed in single quotes ' ', double quotes " ", or triple quotes ''' ''' / """ """ (for multiline).
                   Strings are immutable → once created, you cannot change them, but you can create new ones.

2. list:[1,2,3,"delhi","hello",4.5] A list is a collection of items in Python.
                                    It is ordered, mutable (can be changed), and allows duplicate values.
                                    Defined using square brackets [ ].

3. dictioary. Dictionaries are mutable → you can add, update, or delete items.
4. tuple: A tuple is also a collection of items.
          It is ordered, but immutable (cannot be changed after creation).
          Defined using parentheses ( ).

5. sets: set() or set{}

'''
# question perimeter of square
side_length = 6
perimeter_of_square = 4 * side_length
print(perimeter_of_square) 

'''
1. store the length and width of rectangle and calculate area (decimal allowed)
2. convert celcius temperature 37.5 to faheranite
3. compare two numbers and store the result as a boolean
4. create a ids on codechef
'''
length_of_rectangle = 30.20
width_of_rectangle =  20.00
area_of_rectangle = (length_of_rectangle * width_of_rectangle)
print(area_of_rectangle)

celcius = 37.5
faheranite = 9/5*celcius+32
print("temprature in faheranite:",faheranite)

x = 10
y = 30
result = x > y
print("result:",result)
print(type(result))

# september_3 
# agenda: type conversion (int,float.bool.str,char)

# implicit conversin (do not have to speacify sommthing as float,int,etc)
x = 5
print(type(x))
x = 4.00
print(type(x))
x = "rahul" + "5"  # only string can add mean inside "  "
print(type(x))     

#explicit conversion: int,float,str,bool

x = int(5.9)
print(x)
x = str(5) + str(5.8)  # they do not get add just merge 55.8
print(x)
x = bool(x)
print(x)

print(float(True))
print(str(123) + "abc")
print(int(9.9),float(True),str(123))
print("my name is aryan choudhary and i am",24 + 1,"year old")
print(f"my name is aryan choudhary and i am {24 + 1} year old")

#create a simple calculator which takes random values and perform basic arithmetic operation like +,-,/,%
# enter_first_number = (x)
# enter_second_number = (y)
# the_sum_of_x_and_y = x + y
# the_substraction_of_x_and_y = x - y
# the_division_of_x_and_y = x / y
# the_modulus_of_x_and_y = x % y 

# number_1 = input("enter the first number:")
# print(number_1)
# number_2 = input("enter the second number:")
# print(number_2)

number_1 = float(input("enter the first number:"))
number_2 = float(input("enter the second number:"))
number_1 = int(number_1)
number_2 =int(number_2)
print(f"the sum of {number_1} and {number_2} is {number_1 +number_2}")

#  home work
# form filler
# user enters name,age,marks
name = input("name:")
age = int(input("age:"))
marks = float(input("marks:"))
print(name,age,marks)
print(f"my name is {name} and i am {age} year old and i got{marks} marks")


#lib_name.function_name(*args)


# operators: used to perform operators over the data/ manipulate the data
# operands: values?variables on which operators perform manipulations

import math
a = 1000
b = 1000
sum = a + b * 3/3
# type of operators
# arithmetic operators: +,-,*,%,/

div = math.floor(a/b)
div2 = math.ceil(a/b)
print(div)
print(div2)

#modulus mean reminder
mod = a%b
print(mod)
# exponention a^b
exp = a**b
print(exp)

# question
# given a,b and find a^b such that the answer should not exceed 100007
# 0 <= a,b <= 100

# solution
ans = (a**b)%100007
print(ans)

# ther are some other operators type assignment , comparison ,logical, bitwise , etc read it by your own

# question
# take two integers ans swap them without extra variable

a = 10
b = 20
'''
a,b = b,a   #without extra variable
print(a,b)
'''
# using extra variable
temp = a
a = b
b = temp
print(a,b)
'''
# question

03 take principal amount , rate of interest ,and time in year calculate simple interest

04.Write a program to take the basic salary as
integer input and calculate the total salary,
assuming house rent allowance (HRA) is 20% of basic and travel allowance
•⁠  ⁠(TA) is 10% of basic. 

05.Write a program to take coordinates of two points (x1, y1) and (x2, y2). Calculate the distance between & them using the distance formula.]
'''
# answer 04
basic_salary = int(input("salary:1"))
house_allowance = basic_salary * 0.2
travel_allowance = basic_salary * 0.1
total_salary = basic_salary + travel_allowance + house_allowance
print(total_salary)
# answer 05
# x1 = int(input("x1"))
# x2 = int(input("x2"))
# y1 = int(input("y1"))
# y2= int(input("y2"))
# distance = 


# questions
# Q1:A student enters marks for 3 subjects as strings.
# Convert them to integers and calculate the average.

# Q2: Take a number age = 25.
#⁠  ⁠Convert it into a string and print "My age is 25".

# Q3.A shopping site shows price as string "499.99".
# Add delivery charge (50 as int) and print the final bill.

# 04 Take a complex number z = 5 + 2j.
# Convert it into string.
# Extract real and imaginary parts as integers.
# Print their sum.

# answer_1
subject_1_marks = float(input("subject_1_marks"))
subject_2_marks = float(input("subject_2_marks"))
subject_3_marks = float(input("subject_3_marks"))
average = (int(subject_1_marks) + int(subject_2_marks) + int(subject_3_marks))/3
print(average)
# answer_2
age = str(25)
print((f"my age is {age}"))
# answer_3
price = float("499.99")
price += 50
print(price)
'''
# answer_4
z = str(5 + 2j)
real_part = int(z)
imag_part = float(z)
sum = real_part + imag_part
print(sum)
'''
# question
pen_cost = 12
notebook_cost = 45
total_cost = pen_cost*3 + notebook_cost*4. #write pen_cost and notebook_cost so not do hard code
print(total_cost)
#question
student_score = 78
passing_marks = 40
result = (student_score >= passing_marks)
print("student passed",result)

# class_5 september5 conditonal statements
# if else
'''
if(condition):
   write your instructions here
else :
    write your instruction here 
'''
# question
# given N a number you are supposed to print yes or no based on the fact wheather it is even or odd
N = int(input("enter the number:"))
if N%2 == 0:
      print("yes")
else:
      print("no")
