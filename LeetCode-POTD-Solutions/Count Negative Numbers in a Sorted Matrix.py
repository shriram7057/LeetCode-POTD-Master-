class Solution(object):
    def countNegatives(self, grid):
        count = 0
        n = len(grid[0])
        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += n - left
        return count
