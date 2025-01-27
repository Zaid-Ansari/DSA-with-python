#brute force method to find the maximum subarray sum
arr = [1,2,-33,4,5]
cs = 0
ms = float('-inf')
for i in range(len(arr)):
    for j in range(i,len(arr)):
        cs += arr[j]
        ms = max(cs,ms)
    cs = 0 
print(f"max subarray sum is {ms}")