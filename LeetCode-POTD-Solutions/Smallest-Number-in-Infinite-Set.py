import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1               # next smallest number not yet popped
        self.heap = []              # min-heap for added-back numbers
        self.added = set()          # set to avoid duplicates in heap

    def popSmallest(self):
        # If we have any numbers added back, use them first
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added.remove(smallest)
            return smallest
        
        # Otherwise return the next natural number
        smallest = self.curr
        self.curr += 1
        return smallest

    def addBack(self, num):
        # Only add back numbers < curr that are not already in the heap
        if num < self.curr and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
