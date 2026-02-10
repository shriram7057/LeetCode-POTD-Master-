class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0

        for i, val in enumerate(nums):
            # pivot index condition:
            # left_sum == total - left_sum - val
            if left_sum == total - left_sum - val:
                return i
            left_sum += val

        return -1
