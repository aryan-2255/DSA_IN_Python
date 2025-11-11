total_days = 5
day = 1

while day <= total_days:
    if day == 3:
        day += 1
        continue
    else:
        print("Day:", day)
        user_input = input(f"Enter something for day {day}: ")
        print("You entered:", user_input)
        day += 1



def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:                  # recursive case
        return n * factorial(n - 1)

# take input from user
n = int(input("Enter a number: "))

# call function
f = factorial(n)

print("Factorial of", n, "is", f)