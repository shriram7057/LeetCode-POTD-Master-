class Graph(object):

    def __init__(self, n, edges):
        import heapq
        self.n = n
        self.g = [[] for _ in range(n)]
        for u, v, w in edges:
            self.g[u].append((v, w))

    def addEdge(self, edge):
        u, v, w = edge
        self.g[u].append((v, w))

    def shortestPath(self, node1, node2):
        import heapq
        dist = [10**15] * self.n
        dist[node1] = 0
        pq = [(0, node1)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == node2:
                return d
            for v, w in self.g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        return -1
