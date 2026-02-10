class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        import heapq

        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]

        for a, b, w in edges:
            g[a].append((b, w))
            rg[b].append((a, w))

        def dijkstra(start, graph):
            dist = [10**18] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        d1 = dijkstra(src1, g)
        d2 = dijkstra(src2, g)
        dr = dijkstra(dest, rg)

        ans = 10**18
        for i in range(n):
            if d1[i] < 10**18 and d2[i] < 10**18 and dr[i] < 10**18:
                ans = min(ans, d1[i] + d2[i] + dr[i])

        return ans if ans < 10**18 else -1
