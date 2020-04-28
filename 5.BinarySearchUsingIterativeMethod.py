# You can get the Implementation Video on my Youtube Channel ForCodeCoder

# Binary search is used for searching purpose

################   USing iterative method
def binarySeacrh(start,end,data):
    while end>=start:
        mid = start+(end-start)//2
        if(arr[mid]==data):
            return mid
        elif(arr[mid]>data):
            end = mid -1
        else:
            start = mid+1
    return -1

#  put your data if you have other wise it will create 1 to 49 numbers in arr
# and Binary Search only works with sorted data
arr =[i for i in range(1,50)]
data = 7
res = binarySeacrh(0,len(arr)-1,data)
if(res == -1):
    print("Data not Found..")
else:
    print("Data is present at index {}".format(res))
##################
