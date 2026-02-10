class Solution(object):
    def repeatedNTimes(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
