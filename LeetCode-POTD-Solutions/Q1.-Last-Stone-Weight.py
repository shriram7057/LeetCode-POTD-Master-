import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        # make max-heap by negating values
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # heaviest
            x = -heapq.heappop(heap)  # second heaviest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0
