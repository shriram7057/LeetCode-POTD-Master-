import heapq
from collections import defaultdict

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # DSU
        parent = list(range(c + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for u, v in connections:
            union(u, v)

        # Build min-heap of stations per component
        comp_heap = defaultdict(list)
        for station in range(1, c + 1):
            root = find(station)
            comp_heap[root].append(station)
        for root in comp_heap:
            heapq.heapify(comp_heap[root])

        online = [True] * (c + 1)
        ans = []

        for typ, x in queries:
            if typ == 2:
                # take station x offline (maintenance)
                online[x] = False
            else:  # typ == 1, maintenance check for station x
                if online[x]:
                    ans.append(x)
                else:
                    root = find(x)
                    heap = comp_heap[root]
                    # lazy remove offline stations from heap top
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    ans.append(heap[0] if heap else -1)

        return ans
