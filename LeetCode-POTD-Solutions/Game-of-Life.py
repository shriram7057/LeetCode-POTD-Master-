class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

        def count_live(r, c):
            cnt = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >= m or j >= n:
                        continue
                    if board[i][j] in (1, 3):
                        cnt += 1
            return cnt

        for i in range(m):
            for j in range(n):
                live_neighbors = count_live(i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 3
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
