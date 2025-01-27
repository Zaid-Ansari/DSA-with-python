arr = [1,2,-33,4,5]
cs = 0
ms = float('-inf')
for i in range(len(arr)):
    cs += arr[i]
    ms = max(ms,cs)
    if(cs<0):
        cs = 0
print(f"max subarray sum is {ms}")