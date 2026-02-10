1class Solution:
2    def getDescentPeriods(self, prices):
3        ans = 0
4        streak = 0
5
6        for i in range(len(prices)):
7            if i > 0 and prices[i] == prices[i - 1] - 1:
8                streak += 1
9            else:
10                streak = 1
11            ans += streak
12
13        return ans
14