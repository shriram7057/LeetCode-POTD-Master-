class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        mp = {}
        for i, n in enumerate(nums):
            if n in mp and i - mp[n] <= k:
                return True
            mp[n] = i
        return False
