1class Solution(object):
2    def countPartitions(self, nums):
3        return max(0, len(nums) - 1) if sum(nums) % 2 == 0 else 0
4