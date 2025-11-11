'''
### ticket question

# total_ticket = int(input("total ticket"))
total_ticket = 6
ticket_number = 1 
while total_ticket >= ticket_number:
    print(f"ticket number {ticket_number} issued") 
    ticket_number += 1


### atm withraw question

while True:
    # Prompt the user to enter the withdrawal amount 
    amount = int(input())

    # Check if the amount is a multiple of 100
    if amount % 100 == 0:
       print(f"Withraw of {amount} successful!")

        # Exit the loop after a valid input
       break

        # Else print 'Invalid amount. Please enter a multiple of 100.'
    else:
       print("invalid amount.please enter a multiple of 100")



### round off question

       # Step 1: Original temperature readings
temperature_1 = 23.87654321
temperature_2 = 23.8760
temperature_3 = 23.8769

# Step 2: Round the values to 3 decimal places
reading_1 = round(temperature_1,3)
reading_2 = round(23.8760,3)
reading_3 = round(23.8769,3)

# Step 3: Calculate the average of the rounded temperatures
average_rounded = (reading_1 + reading_2 + reading_3)/3
# Step 4: Calculate the difference in average temperatures
average_original = (temperature_1 + temperature_2 + temperature_3) /3
average_difference = average_original - average_rounded

# Step 5: Print the results
print(f"Rounded Temperature 1: {reading_1}°C")
print(f"Rounded Temperature 2: {reading_2}°C")
print(f"Rounded Temperature 3: {reading_3}°C")
print(f"Average Temperature: {average_rounded}°C")
print(f"Difference in Average Temperature: {average_difference:.3f}°C")
        
### lift decending question

# Step 1: Take user input for the starting level and convert it to an integer
start_level = int(input( ))
# Step 2: Initialize the current level to the user-defined starting level
current_level = start_level
# Step 3: Use a while loop to count down from start_level to 0
while current_level >= 0:
    print(f"Ride descending:Now at Level{current_level}")
    current_level -= 1
# Step 4: Print the final message after reaching the ground
print("The ride has safely reached the ground!")

'''
###. string
 
# index

school = "polaris"
print(school[0])
print(school[4])

# slicing
b = "Hello, World!"
print(b[2:5])

print("aryan-choudhary".split("-"))

# question A { print in one line a  b  c}
a = "scalar school"
print(a[0],a[4],a[12])


# question B. { minus- indexng}
a = "scalar school"
print(a[-1])
print(a[-4])
print(a[-12])

# question C  { split }
a = "political science"
print(a[9:17])

# question D { split }
a = "funda"
print(a[:3])


# reverse the string
s = "aryan choudhary"
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")




# Questionnssss

s = "hello python world"
print(s[12:18])
print(s[9:len(s)-0])

 # replace {here 1 show that replace only 1st word else it replace all}
s = "hello python  world"
s2 = s.replace("world","python",1)
print(s2)

# word count
a = "aryan choudhary"
print(len(a))
