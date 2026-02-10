class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        INF = 10**9
        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd–Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        best = 10**9
        ans = -1

        # Count reachable neighbors
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    cnt += 1

            # smallest count → if tie, choose the LARGER city index
            if cnt <= best:
                best = cnt
                ans = i

        return ans
