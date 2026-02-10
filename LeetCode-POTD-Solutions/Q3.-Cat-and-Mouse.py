class Solution(object):
    def catMouseGame(self, graph):
        n = len(graph)

        # dp[m][c][t]  → result when mouse=m, cat=c, turn=t
        # t = 0 → mouse turn
        # t = 1 → cat turn
        dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        from collections import deque
        q = deque()

        # Base cases
        for i in range(n):
            for t in range(2):
                dp[0][i][t] = 1   # mouse reaches hole → mouse wins
                q.append((0, i, t, 1))

                if i != 0:
                    dp[i][i][t] = 2  # cat catches mouse
                    q.append((i, i, t, 2))

        # degree count
        deg = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        for m in range(n):
            for c in range(n):
                deg[m][c][0] = len(graph[m])                # mouse moves
                deg[m][c][1] = len([x for x in graph[c] if x != 0])  # cat moves (can't go to hole)

        # BFS backward
        while q:
            m, c, t, res = q.popleft()

            # predecessor states
            if t == 0:
                # previous move was cat
                for pc in [x for x in graph[c] if x != 0]:
                    pt = 1
                    if dp[m][pc][pt] == 0:
                        if res == 2:  # cat winning child → cat wins
                            dp[m][pc][pt] = 2
                            q.append((m, pc, pt, 2))
                        else:
                            deg[m][pc][pt] -= 1
                            if deg[m][pc][pt] == 0:
                                dp[m][pc][pt] = 1
                                q.append((m, pc, pt, 1))
            else:
                # previous move was mouse
                for pm in graph[m]:
                    pt = 0
                    if dp[pm][c][pt] == 0:
                        if res == 1:  # mouse winning child → mouse wins
                            dp[pm][c][pt] = 1
                            q.append((pm, c, pt, 1))
                        else:
                            deg[pm][c][pt] -= 1
                            if deg[pm][c][pt] == 0:
                                dp[pm][c][pt] = 2
                                q.append((pm, c, pt, 2))

        return dp[1][2][0]
