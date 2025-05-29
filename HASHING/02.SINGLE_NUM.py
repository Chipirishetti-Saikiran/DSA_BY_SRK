class Solution(object):
    def singleNumber(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1 
            else:
                freq[i]=1    


        for num in arr:
            if freq[num]==1:
                return num 
        return -1            
        