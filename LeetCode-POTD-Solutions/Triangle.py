1class Solution:
2    def minimumTotal(self, triangle):
3        # Start from second-last row and move upward
4        for i in range(len(triangle) - 2, -1, -1):
5            for j in range(len(triangle[i])):
6                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
7
8        return triangle[0][0]
9