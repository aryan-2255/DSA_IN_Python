#1 check is it palindrome or not
num = int(input("enter the number:"))
if num > 0:
    a = str(num)
    nuumber = a[-1:-len(a)-1:-1]
    if nuumber == a:
        print("yes")
    else:
        print("no")
else:
    print("Not Palindrome")


#2 check is it armstrong number or not
num = int(input("enter the number:"))
if num > 0:
    conversion = str(num)
    power = len(conversion)
    a = 0
    for i in conversion:
       a = a + int(i)**power
    if a==num:
        print("yes")
    else:
        print("no")
else:
    print("not a armstrong")

a=[1,2,3,2,3,2,2]
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)