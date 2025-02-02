def findPairSum(arr, target):
    i,j = 0,len(arr)-1
    while(i<j):
        ps = arr[i] + arr[j]
        if ps>target:
            j-=1
        elif ps<target:
            i+=1
        elif ps==target:
            return i, j


#main code
arr = [1,2,3,4,5]
target = 7
a,b = findPairSum(arr, target)
print(str(arr[a]) + " "+ str(arr[b]))

