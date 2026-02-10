1class Solution:
2    def validateCoupons(self, code, businessLine, isActive):
3        allowed = {"electronics", "grocery", "pharmacy", "restaurant"}
4        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
5        
6        valid = []
7        
8        for c, b, a in zip(code, businessLine, isActive):
9            if not a:
10                continue
11            if not c or not all(ch.isalnum() or ch == '_' for ch in c):
12                continue
13            if b not in allowed:
14                continue
15            valid.append((order[b], c))
16        
17        valid.sort()
18        return [c for _, c in valid]
19