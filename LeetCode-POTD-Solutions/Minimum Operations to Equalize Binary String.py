import math

class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        z = s.count('0')

        if z == 0:
            return 0

        if n == k:
            return 1 if z == n else -1

        base = n - k
        res = float('inf')

        # Case 1: x is odd
        odd = max(
            int(math.ceil(float(z) / k)),
            int(math.ceil(float(n - z) / base))
        )
        if odd % 2 == 0:
            odd += 1

        # Case 2: x is even
        even = max(
            int(math.ceil(float(z) / k)),
            int(math.ceil(float(z) / base))
        )
        if even % 2 == 1:
            even += 1

        if (k % 2) == (z % 2):
            res = min(res, odd)

        if z % 2 == 0:
            res = min(res, even)

        return -1 if res == float('inf') else res