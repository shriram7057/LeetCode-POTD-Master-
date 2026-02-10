class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Count each row as a tuple
        row_map = {}
        for row in grid:
            t = tuple(row)
            row_map[t] = row_map.get(t, 0) + 1

        count = 0

        # Build each column as a tuple and match with rows
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            if col in row_map:
                count += row_map[col]

        return count
