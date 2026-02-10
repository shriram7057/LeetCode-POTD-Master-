1class Solution(object):
2    def countTriples(self, n):
3        squares = {i*i: i for i in range(1, n+1)}
4        count = 0
5        
6        for a in range(1, n+1):
7            for b in range(1, n+1):
8                s = a*a + b*b
9                if s in squares and squares[s] <= n:
10                    count += 1
11        
12        return count
13