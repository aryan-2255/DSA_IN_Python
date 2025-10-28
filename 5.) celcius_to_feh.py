# python programm to convet temperature from celcius to faherenhit



# ques

def convertor(cel):
    cel = int(cel)
    feh = (cel*9/5)+32
    print(feh)

try:
 
   x = int(input("celcius"))
   print(convertor(x))
except ValueError:
    print("please input a integer")
else:
    print("no error")
finally:
    print("thank you")


# ques

try:
    temp = float(input("Enter temperature in Celsius: "))

    if temp < -273.15:
        raise ValueError("Temperature below absolute zero is not valid.")

except ValueError as e:
    print(e)  # prints only the error message text

except Exception:
    print("An unknown error occurred.")

else:
    print("The Celsius temperature is:", temp)
    far = (temp * 9/5) + 32
    print("The Fahrenheit temperature is:", far)

finally:
    print("Code is working.")
