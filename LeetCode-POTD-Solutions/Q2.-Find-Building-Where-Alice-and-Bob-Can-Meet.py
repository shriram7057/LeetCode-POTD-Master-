class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        import bisect

        n = len(heights)
        # Normalize queries so a ≤ b
        indexed = []
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            indexed.append((b, a, i))
        indexed.sort(reverse=True)  # sort by b descending

        # Sorted unique heights for compression
        hs = sorted(set(heights))
        m = len(hs)
        # Fenwick tree / BIT storing minimum index for each height rank
        INF = float('inf')
        bit = [INF] * (m + 1)

        def bit_update(i, val):
            while i <= m:
                if val < bit[i]:
                    bit[i] = val
                i += i & -i

        def bit_query(i):
            res = INF
            while i > 0:
                if bit[i] < res:
                    res = bit[i]
                i -= i & -i
            return res if res < INF else -1

        # Process buildings from the end
        res = [-1] * len(queries)
        j = n - 1
        for b, a, qi in indexed:
            # Add buildings with index > b to BIT
            while j > b:
                h = heights[j]
                # rank = position in sorted hs + 1, we want larger heights → lower index in BIT
                rank = m - bisect.bisect_left(hs, h) 
                bit_update(rank, j)
                j -= 1

            if a == b or heights[a] < heights[b]:
                # They can meet at b
                res[qi] = b
            else:
                # Need a building j > b such that heights[j] > heights[a]
                # find all heights > heights[a] i.e. ranks ≤ threshold
                rank_thr = m - bisect.bisect_left(hs, heights[a])
                res[qi] = bit_query(rank_thr - 1)
        return res
