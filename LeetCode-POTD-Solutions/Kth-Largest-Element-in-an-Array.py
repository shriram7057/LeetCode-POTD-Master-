class Solution:
    def findKthLargest(self, nums, k):
        import heapq
        return heapq.nlargest(k, nums)[-1]
