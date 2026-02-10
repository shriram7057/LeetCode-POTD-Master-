class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # 1. Replace all out-of-range numbers with a dummy value (> n)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # 2. Mark existing numbers by negating the index position
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                nums[val - 1] = -abs(nums[val - 1])

        # 3. First positive index + 1 is our answer
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # If all indices are marked, answer is n+1
        return n + 1
