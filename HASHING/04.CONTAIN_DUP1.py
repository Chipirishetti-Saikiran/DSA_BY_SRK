#LEETCODE 217 

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        see=set()
        for i in nums:
            if i in see:
                return True 
            see.add(i)
        return False    
        