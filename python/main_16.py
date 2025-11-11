'''
# list

# append(): list method used to insert/apeend element at the end of the list
l = list()
l.append(4)
l.append(1)
l.append(10)
print(l)

l = list()
print(l)

# another way to declare a list
l2 = []
print(l2)

# get result from list// indexing:
l = ["apple", "banana", "cherry",1,2,5]
l.append('aryan')   # you can see here aryan is added from last
print(l[-1])
l = ["apple", "banana", "cherry",1,2,5]
print(2)

l = ["apple", "banana", "cherry",1,2,5]
l.append('kunal')   # you can see here kunal is added from last
print(l)


# question
list = ['name: aryan','age: 19','school: polaris']
list.append('marks: 400')
print(list[0])
print(list[1])
print(list[2])
print(list[3])



l = ['aryan', 19,'polaris',400]
print(f"name: {l[0]}\nage: {l[1]}\nschool: {l[2]}\nmarks: {l[3]}")

l = ['aryan', 19,'polaris',400]
print(f"name: {l[0]} age: {l[1]} school: {l[2]} marks: {l[3]}")

# question
abcd = ['aryan', 19,'polaris']
abcd.append(400)
print(abcd[0],abcd[1],abcd[2],abcd[3])

# in other way short and good
abcd = ['aryan', 19,'polaris']
abcd.append(400)
for iteam in abcd:
 print(iteam,end=" ")

# lecture_2

N = int(input())
lst = []
for i in range(N):
   num = int(input())
   lst.append(num)
print(lst)
sum = 0
for i in range(N) :
  sum += lst[i]
print(sum)

'''

# list slicing: list_name[start_index:end_index+1]
# l = ['aryan', 19,'polaris',400]
# print(l[1:4])
# print(l[1:])


# n=int(input())
# lst=list()
# for i in range(n):
#     num=int(input())
#     lst.append(num)
# print(lst)
# for i in range (0,n,2):
#     print(lst[i],end=" ")




a = [1,2,3,4,5,'aryan',19,'polaris ']

# pop():remove the last element from the list
a.pop()
print(a)
# remove(): removes the first occurence of a particular element you are passing
a.remove(5)
print(a)  
# count(): counts the number of x elements in the list
a.count((4))
print(a.count(3))
# extend(): extends the list by another list
a.extend([6,7,8])
print(a)  
# reverse(): reverse the order of iteam
a.reverse()
print(a)  
# clear( ): used to clear all elements of the list
a.clear()
print(a)


