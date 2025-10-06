

 # solve queestion on leetcode and talk about subarray,subsequence

prog = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(prog))
a = int(input())
for i in range(0,a):
    for j in range(i,a):
        for k in range(i,j+1):   
         print(prog[k],end=" ")
        print()
        
     
    