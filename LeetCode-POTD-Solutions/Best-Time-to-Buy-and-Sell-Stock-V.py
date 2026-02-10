1class Solution:
2    def maximumProfit(self, prices, k):
3        n = len(prices)
4        if n == 0 or k == 0:
5            return 0
6        
7        INF = 10**18
8        dp0 = [0] + [-INF] * k
9        dp1 = [-INF] * (k + 1)
10        dp2 = [-INF] * (k + 1)
11        
12        for price in prices:
13            new_dp0 = dp0[:]
14            new_dp1 = dp1[:]
15            new_dp2 = dp2[:]
16            
17            for t in range(k + 1):
18                new_dp1[t] = max(new_dp1[t], dp0[t] - price)
19                new_dp2[t] = max(new_dp2[t], dp0[t] + price)
20                
21                if t + 1 <= k:
22                    new_dp0[t + 1] = max(new_dp0[t + 1], dp1[t] + price)
23                    new_dp0[t + 1] = max(new_dp0[t + 1], dp2[t] - price)
24            
25            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2
26        
27        return max(dp0)
28