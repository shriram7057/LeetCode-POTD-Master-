class Solution(object):
    def networkDelayTime(self, times, n, k):
        import heapq

        g = [[] for _ in range(n+1)]
        for u, v, w in times:
            g[u].append((v, w))

        dist = [10**9] * (n+1)
        dist[k] = 0

        pq = [(0, k)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        ans = max(dist[1:])
        return ans if ans < 10**9 else -1
