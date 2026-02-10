class Solution(object):
    def kthFactor(self, n, k):
        factors = []
        i = 1

        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
            i += 1

        factors.sort()
        return factors[k - 1] if k <= len(factors) else -1
