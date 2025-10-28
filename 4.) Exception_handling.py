while True:
    try:
        a = int(input())
        b = int(input())
        res = a/b
    except ZeroDivisionError:
        print("pls dont give 0 to denominator")
        continue                     # Retry input after an error 
    except Exception:
        print("something went wrong")
        continue                     # Retry input after an error 

    else:        # else runs only when the try block succeeds completely — no errors happen 

        print(res)
        break          # if use continue - Uncommon, but would skip cleanup or next logic 

    finally:
        print("my code is running well")
       # continue - if we use continue here {Restarts loop always, even after success }




# try:
#     # code that might throw an error
# except SomeError:
#     # runs if there is an error
# else:
#     # runs only if no error occurred in try
# finally:
#     # always runs no matter what






# BaseException
#  ├── Exception
#  │    ├── ArithmeticError
#  │    │    ├── ZeroDivisionError
#  │    │    └── OverflowError
#  │    ├── ValueError
#  │    ├── TypeError
#  │    ├── NameError
#  │    ├── IndexError
#  │    ├── KeyError
#  │    ├── ImportError
#  │    ├── IOError
#  │    ├── FileNotFoundError
#  │    ├── AssertionError
#  │    └── RuntimeError
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  └── GeneratorExit


# | Category            | Example           | When It Happens       |
# | ------------------- | ----------------- | --------------------- |
# | `ZeroDivisionError` | `5/0`             | Division by zero      |
# | `ValueError`        | `int("abc")`      | Wrong value           |
# | `TypeError`         | `"2" + 2`         | Wrong data type       |
# | `NameError`         | `print(x)`        | Variable not defined  |
# | `IndexError`        | `arr[10]`         | Invalid index         |
# | `KeyError`          | `dict["missing"]` | Missing key           |
# | `ImportError`       | `import xyz`      | Module not found      |
# | `FileNotFoundError` | `open("x.txt")`   | File missing          |
# | `AssertionError`    | `assert x<0`      | Failed check          |
# | `RuntimeError`      | Custom raise      | General runtime issue |
# | `KeyboardInterrupt` | Ctrl+C            | User stopped program  |






# ex:

age = int(input("enter the age:"))

try:
    if(age<18):
        raise ValueError
except ValueError:
    print("plz enter proper age")

else:
    print("you can vote")



# nested try and except method

try:
    try:
        a = int(input())
        b = int(input())
        res = a/b

    except ValueError:
        print("enter valid input")

    except Exception as e:
        print()

except ZeroDivisionError:
    print("enter the deminomenator other than 0")
        
else:
    print(res)

# Final Flow Summary
# Outer Try
#  ├── Runs inner Try
#  │     ├── Executes code
#  │     ├── If inner error → Inner Except (if matches)
#  │     └── If not handled → Goes to Outer Except
#  ├── If error outside inner → Outer Except
#  └── Finally blocks (if any) always run