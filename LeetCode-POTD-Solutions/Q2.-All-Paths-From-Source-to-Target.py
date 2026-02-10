class Solution(object):
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        ans = []

        def dfs(u, path):
            if u == n - 1:
                ans.append(path[:])
                return
            for v in graph[u]:
                dfs(v, path + [v])

        dfs(0, [0])
        return ans
