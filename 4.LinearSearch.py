def LinearSearch(arr,data):
    for i in range(len(arr)):
        if (arr[i] == data):
            print('{} Is present at Index '.format(data), i)
            return
    print("data Is not present")
arr = [2,4,6,7,8,1,0,14,13,15,21,44]
data = 0
LinearSearch(arr,data)
