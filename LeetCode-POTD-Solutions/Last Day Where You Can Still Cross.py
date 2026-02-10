class Solution(object):
    def latestDayToCross(self, row, col, cells):
        from collections import deque

        def canCross(day):
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1

            q = deque()
            visited = [[False]*col for _ in range(row)]
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    visited[0][j] = True

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                x, y = q.popleft()
                if x == row - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return False

        left, right = 0, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
