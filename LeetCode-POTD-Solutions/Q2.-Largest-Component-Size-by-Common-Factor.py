class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        import math

        # ---- DSU ----
        n = max(nums) + 1
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                if size[pa] < size[pb]:
                    pa, pb = pb, pa
                parent[pb] = pa
                size[pa] += size[pb]

        # ---- Prime factorization ----
        def prime_factors(x):
            pf = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    pf.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                pf.add(x)
            return pf

        factor_map = {}

        # Union numbers using their prime factors
        for num in nums:
            factors = prime_factors(num)
            for f in factors:
                if f in factor_map:
                    union(num, factor_map[f])
                else:
                    factor_map[f] = num

        # Count component sizes
        comp = defaultdict(int)
        ans = 1
        for num in nums:
            root = find(num)
            comp[root] += 1
            ans = max(ans, comp[root])

        return ans
