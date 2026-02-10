1class Solution(object):
2    def minDeletionSize(self, strs):
3        m, n = len(strs), len(strs[0])
4        ans = 0
5        
6        for c in range(n):
7            for r in range(1, m):
8                if strs[r][c] < strs[r - 1][c]:
9                    ans += 1
10                    break
11        
12        return ans
13