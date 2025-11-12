# Q-1 Add Digits   ( LeetCode 258   2025-11-12 )



num = int(input("enter the number:"))
sum = num
while (sum > 9):
    sum = 0
    n = num
    # n = 38

    while (n != 0):
        rem = n % 10
        sum = sum + rem
        n = n // 10
    num = sum
print(sum)



# Q-2   (LeetCode )