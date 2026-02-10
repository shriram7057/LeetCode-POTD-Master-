class Solution:
    def countValidSelections(self, nums):
        total = sum(nums)
        valid = 0
        left_sum = 0
        
        for x in nums:
            if x != 0:
                left_sum += x
            else:
                if left_sum * 2 == total:
                    valid += 2
                elif abs(left_sum * 2 - total) == 1:
                    valid += 1
        return valid
