class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        
        freq = Counter(nums)
        return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
