class Solution(object):
    def findFinalValue(self, nums, original):
        nums_set = set(nums)
        while original in nums_set:
            original *= 2
        return original
