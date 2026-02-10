class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        longest = 0
        for n in s:
            if n - 1 not in s:
                length = 1
                while n + length in s:
                    length += 1
                longest = max(longest, length)
        return longest
