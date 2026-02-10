1class Solution(object):
2    def minSubarray(self, nums, p):
3        total = sum(nums)
4        r = total % p
5        if r == 0:
6            return 0
7
8        prefix = 0
9        seen = {0: -1}
10        res = len(nums)
11
12        for i, x in enumerate(nums):
13            prefix = (prefix + x) % p
14            need = (prefix - r) % p
15            if need in seen:
16                res = min(res, i - seen[need])
17            seen[prefix] = i
18
19        return res if res < len(nums) else -1
20