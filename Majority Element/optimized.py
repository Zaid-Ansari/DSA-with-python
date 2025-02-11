arr = [1,6,1,1,6,1,1,7]
freq = 1 
ans = arr[0]
arr.sort()
for i in range(1,len(arr)):
    if arr[i] == arr[i-1]:
        freq += 1
        if (freq > len(arr)//2):
            break
    else:
        freq = 1
        ans = arr[i]
    
    

print("majority element is " + str(ans))