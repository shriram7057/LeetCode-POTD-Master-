1class Solution(object):
2    def maxKDivisibleComponents(self, n, edges, values, k):
3        g = [[] for _ in range(n)]
4        for u, v in edges:
5            g[u].append(v)
6            g[v].append(u)
7
8        visited = [False] * n
9        self.ans = 0
10
11        def dfs(u):
12            visited[u] = True
13            total = values[u]
14            for v in g[u]:
15                if not visited[v]:
16                    sub = dfs(v)
17                    total += sub
18            if total % k == 0:
19                self.ans += 1
20                return 0
21            return total
22
23        dfs(0)
24        return self.ans
25