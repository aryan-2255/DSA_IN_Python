file_name = input("enter file name")
try:
    fs = open(file_name,'r')
    data = fs.read()
except FileNotFoundError:
    print("file do exist")
except PermissionError:
    print("you do not have permission to open the file")
except Exception:
    print("some error")
else:
    print(data)
finally:
    fs.close()
    print("task complete file closed")

