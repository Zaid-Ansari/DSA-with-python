arr = [1,4,6,1,6,6,6,6]
freq = 0 
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(arr[j]==arr[i]):
            freq+=1
    if freq>len(arr)/2:
        print(str(arr[i])+" is the majority element ")
        break
    freq=0
    