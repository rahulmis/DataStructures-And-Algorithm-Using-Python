def Bubble_Sort():
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [2,45,5,1,8,9,1,0,23,11,23,22]
Bubble_Sort()
print(arr)