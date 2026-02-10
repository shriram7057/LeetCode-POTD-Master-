class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # We are allowed to delete only ONE zero
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - 1)  # delete one zero

        return ans
