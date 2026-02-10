class Solution(object):
    def validPath(self, n, edges, source, destination):
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = [False] * n
        stack = [source]
        seen[source] = True

        while stack:
            u = stack.pop()
            if u == destination:
                return True
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)

        return False
