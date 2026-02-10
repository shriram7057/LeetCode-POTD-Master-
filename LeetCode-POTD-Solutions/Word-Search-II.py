class Solution(object):
    def findWords(self, board, words):
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])

        trie = {}
        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = w

        res = []

        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return
            nxt = node[c]
            if '#' in nxt:
                res.append(nxt['#'])
                del nxt['#']
            board[i][j] = None
            for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] is not None:
                    dfs(ni, nj, nxt)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return res
