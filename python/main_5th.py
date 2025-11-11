# class_5 september5 conditonal statements
# if else
'''
if(condition):
   write your instructions here
else :
    write your instruction here 
elif:
    it is use to give another condition midway
'''
# question
# given N a number you are supposed to print yes or no based on the fact wheather it is even or odd
# N = int(input("enter the number:"))
# if N%2 == 0:
#       print("yes")
# else:
#       print("no")
# question
# stored_username = ("admin")
# entered_username = (input("enter your name:")).strip()
# if stored_username == entered_username:
#       print("login succesful")
# else:
#       print("faliure")


# stored_username = ["admin", "shivam", "rohit"]
# entered_username = input("enter your name:").strip()
# if entered_username in stored_username:
#       print("login succesful")
# else:
#       print("faliure")      

age = int(input("Enter the age: - "))

if 0 <= age <= 12:
    print("Ticket price: - 5")

elif 13 <= age <= 64:
    member = input("Do You have membership (Y/N): - ").strip().lower()
    if member == 'y':
        print("Ticket price: - 10")
    else:
        print("Ticket price: - 12")

else:
    print("Ticket price: - 7")
