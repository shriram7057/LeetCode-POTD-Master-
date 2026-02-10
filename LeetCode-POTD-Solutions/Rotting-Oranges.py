from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        time = 0
        
        while q:
            i, j, t = q.popleft()
            time = max(time, t)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    q.append((ni, nj, t + 1))
        
        return time if fresh == 0 else -1
