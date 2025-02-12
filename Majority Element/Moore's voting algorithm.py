def mooreAlgo(arr):
    freq = 0 
    ans = None
    for i in arr:
        if freq == 0:
            ans = i
        if ans == i:
            freq += 1
        else:
            freq -= 1

    count = arr.count(ans)
    if count > len(arr) // 2:   
        print("Majority element is " + str(ans))
    else:
        print("No majority element")

#main
arr = [1,1,6,1,1,6,1,7]
mooreAlgo(arr)