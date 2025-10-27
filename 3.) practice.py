
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


#3 find prime factor divisor of an input
num = int(input("enter the number"))
my_list =[]
for i  in range(2,num+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
           if num%i == 0:
                my_list.append(i)
print(my_list)


#4 frequency map / dupicates
arr = [1,2,2,3,3,3,4,5,5,5,5]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)


#5 max subarray's (brute force and kadane)
#1 brute force
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = float('-inf')
for i in range(len(arr)):
    for j in range (i,len(arr)):
        current_sum = sum(arr[i:j+1])
        max_sum = max(current_sum,max_sum)
print(max_sum)

#2 kadane theorm
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum + arr[i])
        max_sum = max(current_sum,max_sum)

    return max_sum


something = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(something))

#3 max product subarray
def max_product_subarray(arr):
    current_max = current_min = result = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            current_max, current_min = current_min, current_max
        current_max = max(arr[i], arr[i] * current_max)
        current_min = min(arr[i], arr[i] * current_min)
        result = max(result, current_max)
    return result

arr = [2,3,-2,4]
print(max_product_subarray(arr)) 


#6 two pointer

arr = [1, 2, 3, 4, 6, 8, 9]
target = 10

i = 0
j = len(arr) - 1

while i < j:
    total = arr[i] + arr[j]
    
    if total == target:
        print("Pair found:", arr[i], arr[j])
        break
    elif total < target:
        i += 1   # move i forward to increase sum
    else:
        j -= 1   # move j backward to decrease sum


#7 prefix
arr = [2, 4, 6, 8, 10]
prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)  # [2, 6, 12, 20, 30]
# Using Prefix Sum (if you need running totals)
arr = [2, 4, 6, 8, 10]
prefix = []
total = 0

for num in arr:
    total += num
    prefix.append(total)

print(prefix)  # [2, 6, 12, 20, 30]

#8 Reverse an Array | Practice 
class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            # swap the elements
            arr[left], arr[right] = arr[right], arr[left]
            
            # move the pointers
            left += 1
            right -= 1
        
        return arr
