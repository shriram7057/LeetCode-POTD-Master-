1class Solution:
2    def combinationSum4(self, nums, target):
3        dp = [0] * (target + 1)
4        dp[0] = 1
5
6        for t in range(1, target + 1):
7            for num in nums:
8                if t >= num:
9                    dp[t] += dp[t - num]
10
11        return dp[target]
12