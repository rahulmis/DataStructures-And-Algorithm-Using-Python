def Selection_Sort():
    n = len(arr)
    for i in range(n):
        min_val = i
        for j in range(i+1,n):
            if(arr[min_val]>arr[j]):
                min_val = j
        arr[min_val],arr[i] = arr[i],arr[min_val]

arr = [2,45,5,1,8,9,1,0,23,11,23,22]
Selection_Sort()
print(arr)