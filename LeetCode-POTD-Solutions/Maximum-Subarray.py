class Solution(object):
    def maxSubArray(self, nums):
        cur = ans = nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)
            ans = max(ans, cur)
        return ans
