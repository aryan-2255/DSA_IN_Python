#  talk about time and space complaxity , types and codechef base question

# # import array as arr
# a = arr.array('i', [1,2,3,4,5])
# print(a)
# print(type(a))
# a = arr.array('f', [1,2,3,4,5])
# print(a)
# print(type(a))


import array as arr

a = arr.array('i', [1,2,3,4,5,5,5])
a.append(6)       # use to insert value from last
a.insert(2,1110)  # use to insert value while using index can tell the position
a.pop(-2)         # use when you give  index
a.remove(4)       # use when you know which element to be removed
a.reverse()       # use to reverse the array
print(a.count(5))  # count the no.
print(a.index(1))  # tell the position
a.extend([100,200,300])

print(a)
print(type(a))
