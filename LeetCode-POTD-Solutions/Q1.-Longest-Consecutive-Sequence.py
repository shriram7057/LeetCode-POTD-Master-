class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        s = set(nums)
        best = 0

        for x in s:
            # only start counting when x is the beginning of a sequence
            if x - 1 not in s:
                length = 1
                cur = x + 1
                while cur in s:
                    length += 1
                    cur += 1
                if length > best:
                    best = length

        return best
