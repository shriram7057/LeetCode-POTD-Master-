class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        import heapq
        n = len(values)
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))

        dist = [10**18] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, t in g[u]:
                nd = d + t
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        used = [0] * n
        ans = [0]  # use list to avoid nonlocal (works in Python2/3)

        def dfs(u, time, score):
            if used[u] == 0:
                score += values[u]
            used[u] += 1

            if u == 0:
                if score > ans[0]:
                    ans[0] = score

            for v, t in g[u]:
                nt = time + t
                if nt <= maxTime and nt + dist[v] <= maxTime:
                    dfs(v, nt, score)

            used[u] -= 1

        dfs(0, 0, 0)
        return ans[0]
