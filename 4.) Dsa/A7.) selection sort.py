def selectionsort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min_ind = i 
        for j in range(i+1,n):
            if(arr[j]<arr[min_ind]):
                min_ind = j
        arr[min_ind],arr[i] = arr[i] , arr[min_ind]


arr = [1,6,3,2,10,9]

selectionsort(arr)

print(arr)