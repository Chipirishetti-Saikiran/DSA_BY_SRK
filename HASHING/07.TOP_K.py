#LEETCODE 347
class Solution(object):
    def topKFrequent(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1  
        
        
        top_k = sorted(freq, key=freq.get, reverse=True)[:k]
        return top_k
        