class Solution(object):
    def summaryRanges(self, nums):
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
            i += 1
        return res
