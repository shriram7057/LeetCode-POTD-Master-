class Solution(object):
    def waysToMakeFair(self, nums):
        n = len(nums)

        # prefix sums for even and odd indices
        preE = [0] * (n + 1)
        preO = [0] * (n + 1)

        for i in range(n):
            preE[i+1] = preE[i]
            preO[i+1] = preO[i]
            if i % 2 == 0:
                preE[i+1] += nums[i]
            else:
                preO[i+1] += nums[i]

        res = 0

        for i in range(n):
            # remove nums[i]
            # left evens = preE[i]
            # left odds = preO[i]

            # after removal, right side indices shift (even ↔ odd)
            right_even = preO[n] - preO[i+1]   # originally odd → now even
            right_odd  = preE[n] - preE[i+1]   # originally even → now odd

            if preE[i] + right_even == preO[i] + right_odd:
                res += 1

        return res
