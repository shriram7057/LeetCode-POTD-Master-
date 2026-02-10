class Solution(object):
    def minCostConnectPoints(self, points):
        import heapq

        n = len(points)
        used = [False] * n
        heap = [(0, 0)]   # (cost, point)
        ans = 0
        taken = 0

        while taken < n:
            cost, u = heapq.heappop(heap)
            if used[u]:
                continue
            used[u] = True
            ans += cost
            taken += 1

            x1, y1 = points[u]
            for v in range(n):
                if not used[v]:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, v))

        return ans
