def LinearSearch(arr, data):
    # create a for loop so we can check every element
    for i in range(len(arr)):
        # check if data is equals to i index of array
        if (arr[i] == data):
            print('{} Is present at Index : '.format(data), i)
            # if equals then print and stop the loop
            return
    # if data is not in the array then print
    print("Data Is not present")

# Create a list of elements in which we have
# to perform Linear Search
arr = [2, 4, 6, 7, 8, 1, 0, 14, 13, 15, 21, 44]
# creating a while loop so we can search data
# many times
while True:
    # take input data which user want to search
    data = int(input("Enter Data For Linear Search : "))
    # call the linearsearch function to check data
    # data is present or not
    LinearSearch(arr, data)
