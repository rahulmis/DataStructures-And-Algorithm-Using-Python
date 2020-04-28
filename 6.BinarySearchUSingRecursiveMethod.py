######################  Using Recursion method
# You can get the Implementation Video on my Youtube Channel ForCodeCoder

def binarySeacrh(start,end,data):
    if(end>=start):
        mid =start+(end-start)//2
        if(arr[mid]==data):
            return mid
        elif(arr[mid]>data):
            return binarySeacrh(start,mid-1,data)
        else:
            return binarySeacrh(mid+1,end, data)
    return -1

# Binary search only works in sorted data
arr =[1,2,11,22,33,44,55,61,62,62,67,68]
data = 44
res = binarySeacrh(0,len(arr)-1,data)
if(res == -1):
    print("Data not Found..")
else:
    print("Data is present at index {}".format(res))
