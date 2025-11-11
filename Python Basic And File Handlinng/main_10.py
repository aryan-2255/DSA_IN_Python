
# function
def name_of_function(*args):
    pass
# Q-1 : write afunction to perform addition of two integers a and b
# def addition(a,b):
#     sum = a + b
#     return sum

# c = 5
# d = 4
# s = addition(c,d)
# print(s)


# Q-2: write a function greet (name) that print personalised greeting message
def greet(name):
    print((f"welcome to polris school of technology mr.{name}"))
name = input("enter the person name: ")
greet(name)


# Q-3: write a function add(a,b)that takes two numbers and prints theiir sum.
# def add(a,b):
#     print(f"the sum of {a} and {b} is {sum}")
# a = int(input('enter first no.'))
# b = int(input("enter second number"))
#  calling the function 
# add(a,b)

# Q-4: write a function square(num) that returns the square of a number
# def square(num):
#     sq = num**2
#     return sq
# num = int(input("enter no."))
# sq = square(num)
# print(sq)


'''
Use return when you want the function to give back a value for further use.

Use print when you just want to show output.

sq = square(num) stores the result, so you can use it multiple times.
'''
# def area_and_perimeter(length,width):
#     area = length*width
#     perimeter = 2*(length + width)
#     return area,perimeter
# length = int(input("enter a"))
# width = int(input("enter b"))
# print(f"area and perimeter of {length} and {width} is {area},{perimeter}")???????????????solve




# # Q. wrie a functional factorial (n) that returns factorial of a number  
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# n=5
# factorial(n)

# # global variable can not be modified in local scope
# a= 10
# a+=10
# print(a)
# def sqrt(n):
#     global a 
#     a = a+4
#     print(a)
#     b = 50
#     print(b)


# sqrt(20)
# print(a)
# # b is present in the local scope
# # print(b)

# # arguments:
# #1. positional arguments
# def substract(a,b):
#     print(a-b)


# a = 2
# b = 3 
# substract(a,b) #correct
# substract(b,a) #incorrect

# # 3. Default arguments 
# def substract(a=2,b=3):
#     print(a-b)
# substract(5,5)


# Q-: write a function that takes marks of 5 subject and return total and average.
# def total_average(a,b,c,d,e):
#     total = a + b + c + d + e
#     average = (a + b + c + d + e) /5
#     return total,average
# a = int(input("a--"))
# b = int(input("b--"))
# c = int(input("c--"))
# d = int(input("d--"))
# e = int(input("e--"))
# total,average = total_average(a,b,c,d,e)
# print(total,average)


def reverse_integer(n):
    rev_n = 0
    while n != 0:
        rev_n = rev_n*100 + n%10
        n //= 10
        return rev_n
    

n = int(input("enter an integer:"))
rev_n = reverse_integer
print(rev_n)
    