class Solution(object):
    def construct(self, grid):
        n = len(grid)

        def same(x1, y1, size):
            val = grid[x1][y1]
            for i in range(x1, x1 + size):
                for j in range(y1, y1 + size):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def build(x, y, size):
            uniform, val = same(x, y, size)
            if uniform:
                return Node(val == 1, True)

            half = size // 2
            return Node(
                True,
                False,
                build(x, y, half),
                build(x, y + half, half),
                build(x + half, y, half),
                build(x + half, y + half, half)
            )

        return build(0, 0, n)
