1import heapq
2
3class Solution:
4    def minCost(self, grid, k):
5        m, n = len(grid), len(grid[0])
6        INF = 10**18
7
8        # dist[i][j][t] = min cost to reach (i,j) using t teleports
9        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
10        dist[0][0][0] = 0
11
12        # All cells sorted by value
13        cells = []
14        for i in range(m):
15            for j in range(n):
16                cells.append((grid[i][j], i, j))
17        cells.sort()
18
19        # For each teleport layer, pointer over sorted cells
20        ptr = [0] * (k + 1)
21
22        # Dijkstra: (cost, i, j, t)
23        pq = [(0, 0, 0, 0)]
24
25        while pq:
26            d, i, j, t = heapq.heappop(pq)
27            if d != dist[i][j][t]:
28                continue
29
30            # Normal move: right
31            if j + 1 < n:
32                nd = d + grid[i][j + 1]
33                if nd < dist[i][j + 1][t]:
34                    dist[i][j + 1][t] = nd
35                    heapq.heappush(pq, (nd, i, j + 1, t))
36
37            # Normal move: down
38            if i + 1 < m:
39                nd = d + grid[i + 1][j]
40                if nd < dist[i + 1][j][t]:
41                    dist[i + 1][j][t] = nd
42                    heapq.heappush(pq, (nd, i + 1, j, t))
43
44            # Teleport
45            if t < k:
46                while ptr[t] < len(cells) and cells[ptr[t]][0] <= grid[i][j]:
47                    _, x, y = cells[ptr[t]]
48                    if d < dist[x][y][t + 1]:
49                        dist[x][y][t + 1] = d
50                        heapq.heappush(pq, (d, x, y, t + 1))
51                    ptr[t] += 1
52
53        ans = min(dist[m - 1][n - 1])
54        return -1 if ans == INF else ans
55