class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (backtrack(r+1, c, i+1) or
                     backtrack(r-1, c, i+1) or
                     backtrack(r, c+1, i+1) or
                     backtrack(r, c-1, i+1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
