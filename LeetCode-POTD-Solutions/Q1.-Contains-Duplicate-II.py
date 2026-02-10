class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last = {}

        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                return True
            last[num] = i

        return False
