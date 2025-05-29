def TWO_SUM(arr,tar):
    num_map={}
    for i,num in enumerate(arr):
        remain=tar-num 
        if remain in num_map:
            return [num_map[remain],i]
        num_map[remain]=i 
    return -1