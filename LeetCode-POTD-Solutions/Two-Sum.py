class Solution(object):
    def twoSum(self, nums, target):
        mp = {}
        for i, n in enumerate(nums):
            if target - n in mp:
                return [mp[target - n], i]
            mp[n] = i
