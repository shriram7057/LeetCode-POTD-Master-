1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        if not matrix or not matrix[0]:
4            return False
5
6        m, n = len(matrix), len(matrix[0])
7        left, right = 0, m * n - 1
8
9        while left <= right:
10            mid = left + (right - left) // 2
11            row = mid // n
12            col = mid % n
13            val = matrix[row][col]
14
15            if val == target:
16                return True
17            elif val < target:
18                left = mid + 1
19            else:
20                right = mid - 1
21
22        return False
23