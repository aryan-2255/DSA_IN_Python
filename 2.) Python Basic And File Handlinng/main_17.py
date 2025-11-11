# tuples
tpl = ()
print(type(tpl))

# ordered data type
tpl1 = (1,2,3)
tpl2 = (1,3,2)
print(tpl1,tpl2)

# accessing elements / indexing or slicing
tpl1 = (1,2,3)
tpl2 = (1,7,2,5)
print(tpl1[1])
print(tpl1[2])
print(tpl1[0:2])
print(tpl2[3])
print(tpl2[-2])



tpl3 = 2,3,4,5,6.2,'aryan',[8,7,9]       # tuple also store hetrogenuous data
print(tpl3)
# immutability : element stored cannot be changed:
print(tpl3)
l = tpl3[6]
print(l)
l[0] = 100
print(tpl3)


# questions

user_input = input("destination:")
tpl = user_input.strip()
list = tpl.split(',')
list = tuple(list)
print(f"Tuple of favorite travel destinations:{list}")


# tuple(arg): converts the argument into tuple

# tuple concatenation: (+) used to concatenate tuples in the order they are
tpl1 = (11,22,33)
tpl2 = (44,55,66)
print(tpl1,tpl2)
tpl3 = tpl1 + tpl2
print(tpl3)
# tuple multiplication:
print(tpl3*3)

#)tuple membership:(in , not in)
print(44 in tpl3)
print(44 not in tpl3)

# iteration:
for iteam in tpl3:
    print(iteam,end="//")

# count(arg): count the number of element appears
t = (0,0,9,8,7)
print(t.count(0))
# index(): inorder to fnd the first index of a perticular element
print(t.index(8))