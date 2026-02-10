class Solution(object):
    def countCompleteComponents(self, n, edges):
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = [False] * n

        def dfs(u, comp):
            stack = [u]
            seen[u] = True
            while stack:
                x = stack.pop()
                comp.append(x)
                for v in g[x]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)

        ans = 0
        for i in range(n):
            if not seen[i]:
                comp = []
                dfs(i, comp)
                k = len(comp)
                edge_count = 0
                for x in comp:
                    edge_count += len(g[x])
                edge_count //= 2
                if edge_count == k * (k - 1) // 2:
                    ans += 1

        return ans
