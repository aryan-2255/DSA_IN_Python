# question
n = 836
sum=0
while(n>0) or sum>10:
    if(n==0):
        n=sum
        sum=0
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)


# file handling
#syntax
# f = open('demo.txt','r')
# data = f.read()
# print(data)



f = open("read.txt","r")
# data = f.read()
# print(data)

# data = f.readline( )
# print(data)

# data = f.readlines()
# print(data)




