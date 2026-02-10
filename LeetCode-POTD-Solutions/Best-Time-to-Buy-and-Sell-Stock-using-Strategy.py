1class Solution(object):
2    def maxProfit(self, prices, strategy, k):
3        n = len(prices)
4        base = sum(prices[i] * strategy[i] for i in range(n))
5        half = k // 2
6        
7        remove = [-strategy[i] * prices[i] for i in range(n)]
8        sell_gain = [prices[i] - strategy[i] * prices[i] for i in range(n)]
9        
10        pref_remove = [0] * (n + 1)
11        pref_sell = [0] * (n + 1)
12        
13        for i in range(n):
14            pref_remove[i + 1] = pref_remove[i] + remove[i]
15            pref_sell[i + 1] = pref_sell[i] + sell_gain[i]
16        
17        best = 0
18        for i in range(n - k + 1):
19            cur = (pref_remove[i + half] - pref_remove[i]) \
20                + (pref_sell[i + k] - pref_sell[i + half])
21            best = max(best, cur)
22        
23        return base + best
24