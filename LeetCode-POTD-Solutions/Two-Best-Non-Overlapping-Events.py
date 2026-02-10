1class Solution(object):
2    def maxTwoEvents(self, events):
3        events.sort()
4        import heapq
5        
6        heap = []
7        best = 0
8        ans = 0
9        
10        for start, end, value in events:
11            while heap and heap[0][0] < start:
12                best = max(best, heapq.heappop(heap)[1])
13            ans = max(ans, best + value)
14            heapq.heappush(heap, (end, value))
15        
16        return ans
17