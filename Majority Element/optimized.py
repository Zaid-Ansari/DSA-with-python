def majEle(arr):

    arr.sort()
    freq = 1 
    ans = arr[0]
    
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            freq += 1
        
        else:
            freq = 1
            ans = arr[i]
        
        if (freq > len(arr)//2):
                break

    count = arr.count(ans)
    if count <= len(arr) // 2:
        print("No majority element")
        return
    print("Majority element is " + str(ans))    

#main    
arr = [1,6,1,1,6,1,1,7]
majEle(arr)

