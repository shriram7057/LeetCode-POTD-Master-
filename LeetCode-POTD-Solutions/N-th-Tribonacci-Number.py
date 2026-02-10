1class Solution(object):
2    def tribonacci(self, n):
3        if n == 0:
4            return 0
5        if n == 1 or n == 2:
6            return 1
7
8        a, b, c = 0, 1, 1
9        for _ in range(3, n + 1):
10            d = a + b + c
11            a, b, c = b, c, d
12
13        return c
14