1class Solution(object):
2    def countTrapezoids(self, points):
3        from collections import Counter
4        MOD = 1000000007
5        
6        ycnt = Counter()
7        for x, y in points:
8            ycnt[y] += 1
9
10        total = 0
11        prev_pairs = 0
12
13        for y in sorted(ycnt):
14            c = ycnt[y]
15            if c >= 2:
16                curr = c * (c - 1) // 2
17                total = (total + prev_pairs * curr) % MOD
18                prev_pairs = (prev_pairs + curr) % MOD
19
20        return total % MOD
21