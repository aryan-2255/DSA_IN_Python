# searching algorithms - A searching algorithm is a method used to find the position or existence of a particular element (called a key) in a collection of data (like an array, list, or database).

# 1. Linear Search

# Check each element one by one until the target is found.

# Works on unsorted or sorted data.

##        Algorithm Steps:

# Start from the first element.

# Compare each element with the target.

# If found, return its position.

# If not found after checking all, return -1.



#  Time Complexity:
# Best: O(1)
# Worst: O(n)


# example -

#1.)
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


#2.)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
target = 3
print(linear_search(arr, target))