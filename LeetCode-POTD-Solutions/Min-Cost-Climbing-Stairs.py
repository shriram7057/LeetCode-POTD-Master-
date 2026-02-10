1class Solution(object):
2    def minCostClimbingStairs(self, cost):
3        n = len(cost)
4        if n == 2:
5            return min(cost[0], cost[1])
6
7        a, b = cost[0], cost[1]  # a = cost to reach step 0, b = cost to reach step 1
8
9        for i in range(2, n):
10            c = min(a, b) + cost[i]
11            a, b = b, c
12
13        return min(a, b)
14