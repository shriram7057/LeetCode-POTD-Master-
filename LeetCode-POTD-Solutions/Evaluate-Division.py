class Solution(object):
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque

        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            q = deque([(start, 1.0)])
            visited = set([start])

            while q:
                node, val = q.popleft()
                if node == end:
                    return val
                for nei, w in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, val * w))

            return -1.0

        return [bfs(a, b) for a, b in queries]
