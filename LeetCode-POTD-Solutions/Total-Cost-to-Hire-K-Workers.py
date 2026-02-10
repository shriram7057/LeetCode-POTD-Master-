import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        left = []   # heap for left side
        right = []  # heap for right side

        i, j = 0, n - 1
        total = 0

        # Load initial candidates into heaps
        while i <= j and len(left) < candidates:
            heapq.heappush(left, costs[i])
            i += 1

        while j >= i and len(right) < candidates:
            heapq.heappush(right, costs[j])
            j -= 1

        # Hire k workers
        for _ in range(k):
            # Decide from which heap to pick
            if right and left:
                if left[0] <= right[0]:
                    total += heapq.heappop(left)
                    if i <= j:
                        heapq.heappush(left, costs[i])
                        i += 1
                else:
                    total += heapq.heappop(right)
                    if i <= j:
                        heapq.heappush(right, costs[j])
                        j -= 1

            elif left:   # Only left heap has items
                total += heapq.heappop(left)
                if i <= j:
                    heapq.heappush(left, costs[i])
                    i += 1

            else:        # Only right heap has items
                total += heapq.heappop(right)
                if i <= j:
                    heapq.heappush(right, costs[j])
                    j -= 1

        return total
