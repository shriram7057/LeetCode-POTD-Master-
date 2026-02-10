1class Solution:
2    def change(self, amount: int, coins):
3        dp = [0] * (amount + 1)
4        dp[0] = 1
5
6        for coin in coins:
7            for x in range(coin, amount + 1):
8                dp[x] += dp[x - coin]
9
10        return dp[amount]
11