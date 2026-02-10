class Solution(object):
    def findTargetSumWays(self, nums, target):
        from collections import defaultdict

        dp = defaultdict(int)
        dp[0] = 1

        for x in nums:
            ndp = defaultdict(int)
            for s in dp:
                ndp[s + x] += dp[s]
                ndp[s - x] += dp[s]
            dp = ndp

        return dp[target]
