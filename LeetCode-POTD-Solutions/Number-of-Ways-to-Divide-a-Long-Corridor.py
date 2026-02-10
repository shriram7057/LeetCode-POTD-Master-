1class Solution:
2    def numberOfWays(self, corridor: str) -> int:
3        MOD = 10**9 + 7
4        
5        seats = [i for i, c in enumerate(corridor) if c == 'S']
6        total = len(seats)
7        
8        if total == 0 or total % 2 == 1:
9            return 0
10        
11        ways = 1
12        for i in range(2, total, 2):
13            gap = seats[i] - seats[i - 1]
14            ways = (ways * gap) % MOD
15        
16        return ways
17