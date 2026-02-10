import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
