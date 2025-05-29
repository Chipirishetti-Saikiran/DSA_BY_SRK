#LEETCODE 219


class Solution(object):
    def containsNearbyDuplicate(self, arr, k):
        seen = set()
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            seen.add(arr[i])
            if len(seen) > k:
                seen.remove(arr[i - k])
        return False
