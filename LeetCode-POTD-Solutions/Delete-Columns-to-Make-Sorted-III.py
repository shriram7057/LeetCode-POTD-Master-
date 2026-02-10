1class Solution(object):
2    def minDeletionSize(self, strs):
3        n = len(strs)
4        m = len(strs[0])
5        
6        dp = [1] * m
7        
8        for j in range(m):
9            for i in range(j):
10                ok = True
11                for r in range(n):
12                    if strs[r][i] > strs[r][j]:
13                        ok = False
14                        break
15                if ok:
16                    dp[j] = max(dp[j], dp[i] + 1)
17        
18        return m - max(dp)
19