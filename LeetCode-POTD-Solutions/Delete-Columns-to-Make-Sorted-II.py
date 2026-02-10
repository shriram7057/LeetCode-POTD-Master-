1class Solution(object):
2    def minDeletionSize(self, strs):
3        n, m = len(strs), len(strs[0])
4        deleted = 0
5        sorted_rows = [False] * (n - 1)
6
7        for col in range(m):
8            bad = False
9            for i in range(n - 1):
10                if not sorted_rows[i] and strs[i][col] > strs[i + 1][col]:
11                    bad = True
12                    break
13
14            if bad:
15                deleted += 1
16            else:
17                for i in range(n - 1):
18                    if strs[i][col] < strs[i + 1][col]:
19                        sorted_rows[i] = True
20
21        return deleted
22