class Solution(object):
    def minEatingSpeed(self, piles, h):
        import math

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            # Compute hours required at speed mid
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid   # same as math.ceil(p / mid)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
