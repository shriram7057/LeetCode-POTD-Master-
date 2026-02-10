class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        res = 0
        steps = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                steps += 1
            res += steps

        return res
