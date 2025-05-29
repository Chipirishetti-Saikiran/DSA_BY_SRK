#BRUTE FORCE
def First_Unique(arr):
    n=len(arr)
    for i in range(n):
        unique=True 
        for j in range(n):
            if i!=j and arr[i]==arr[j]:
                unique=False 
                break 
        if unique:
            return arr[i]
    return -1  

#OPTIMAL
def First_Unique(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1 
        else:
            freq[i]=1 
    for j in arr:
        if freq[j]==1:
            return j 
    return -1                        