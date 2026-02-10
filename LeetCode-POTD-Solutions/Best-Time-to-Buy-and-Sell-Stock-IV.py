1class Solution(object):
2    def maxProfit(self, k, prices):
3        n = len(prices)
4        if n < 2 or k == 0:
5            return 0
6
7        # If k is large enough, the problem becomes unlimited transactions
8        if k >= n // 2:
9            profit = 0
10            for i in range(1, n):
11                if prices[i] > prices[i-1]:
12                    profit += prices[i] - prices[i-1]
13            return profit
14
15        # DP arrays
16        buy = [-float('inf')] * (k + 1)
17        sell = [0] * (k + 1)
18
19        for price in prices:
20            for t in range(1, k + 1):
21                buy[t] = max(buy[t], sell[t - 1] - price)
22                sell[t] = max(sell[t], buy[t] + price)
23
24        return sell[k]
25