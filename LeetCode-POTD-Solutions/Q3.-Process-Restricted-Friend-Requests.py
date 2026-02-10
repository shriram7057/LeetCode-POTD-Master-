class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """

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

        ans = []

        # For each request:
        for u, v in requests:
            pu = find(u)
            pv = find(v)

            can_merge = True

            # Check all restrictions
            for a, b in restrictions:
                pa = find(a)
                pb = find(b)

                # If merging u & v causes a forbidden pair to be in same group → reject
                if (pa == pu and pb == pv) or (pa == pv and pb == pu):
                    can_merge = False
                    break

            if can_merge:
                union(pu, pv)
                ans.append(True)
            else:
                ans.append(False)

        return ans
