class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        # Move all non-zero elements to the front
        for n in nums:
            if n != 0:
                nums[insert_pos] = n
                insert_pos += 1

        # Fill remaining positions with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
