class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        from collections import deque

        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]

        for a, b in redEdges:
            red[a].append(b)
        for a, b in blueEdges:
            blue[a].append(b)

        dist = [[10**9] * 2 for _ in range(n)]
        dist[0][0] = 0
        dist[0][1] = 0

        q = deque()
        q.append((0, 0))  # red last
        q.append((0, 1))  # blue last

        while q:
            node, color = q.popleft()
            d = dist[node][color]

            if color == 0:
                for nxt in blue[node]:
                    if d + 1 < dist[nxt][1]:
                        dist[nxt][1] = d + 1
                        q.append((nxt, 1))
            else:
                for nxt in red[node]:
                    if d + 1 < dist[nxt][0]:
                        dist[nxt][0] = d + 1
                        q.append((nxt, 0))

        ans = []
        for r, b in dist:
            m = min(r, b)
            ans.append(m if m < 10**9 else -1)

        return ans
