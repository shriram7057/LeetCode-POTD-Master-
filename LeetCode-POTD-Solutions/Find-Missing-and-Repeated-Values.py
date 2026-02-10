class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        seen = set()
        repeated = missing = -1
        total = n * n
        nums = [num for row in grid for num in row]

        for num in nums:
            if num in seen:
                repeated = num
            seen.add(num)

        for i in range(1, total + 1):
            if i not in seen:
                missing = i
                break

        return [repeated, missing]
