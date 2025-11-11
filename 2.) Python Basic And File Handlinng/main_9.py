# fibonacci series
'''
n =int(input())
a = 0
b = 1
c = a + b
# update a nad b
a = b
b = c
c = a + b
# update a and b
a = b
b = c
c = a + b
print(a)
print(b)
for i in range(2,n):
    c = a+b
    print(c)
    a = b
    b = c
    c = a + b


# find greater value on putting the three integers 

a = int(input("no.1"))
b = int(input("no.2"))
c = int(input("no.3"))

# print(max(a,b,c)).   methos_1

if a >= b and a >= c:
    print(a)  
elif b >= c and b >= a:
    print(b)
else:
     print(c) 


'''


'''

year = int(input("enter year:"))
if year%400 == 0:
  print("leap year")
elif year%4 == 0:
  print("leap year")
elif year%100 != 0: 
  print("non leap year")
else:
  print("non leap year")

year = int(input("enter year:"))
if (year%400 == 0) or (year%4 == 0) and (year%100 != 0):
 print("leap year")
else:
  print("non leap year")

'''
# generate  random number between a and b and there are lots random.etc find it by your own?
# import random
# print(random.randint(1,100))



import random

while True:
    user_move = input("Enter Rock, Paper, Scissors or Quit: ")
    if user_move == "quit":
        break

    number = random.randint(0, 2)

    if number == 0:
        print("Rock")
        if user_move == "Rock":
            print("Draw!")
        elif user_move == "Scissors":
            print("Computer wins!")
        else:
            print("User wins!")

    elif number == 1:
        print("Scissors")
        if user_move == "Rock":
            print("User wins!")
        elif user_move == "Scissors":
            print("Draw!")
        else:
            print("Computer wins!")

    else:
        print("Paper")
        if user_move == "Rock":
            print("Computer wins!")
        elif user_move == "Scissors":
            print("User wins!")
        else:
            print("Draw!")
          