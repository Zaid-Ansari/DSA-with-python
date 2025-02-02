def findPairSum(arr, target):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j] == target:
                return i, j

#main code
arr = [1,2,3,4,5]
target = 7
a,b = findPairSum(arr, target)
print(str(arr[a]) + " "+ str(arr[b]))

