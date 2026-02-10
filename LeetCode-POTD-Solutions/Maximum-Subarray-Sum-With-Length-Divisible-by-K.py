1class Solution(object):
2    def maxSubarraySum(self, nums, k):
3        import bisect
4        n = len(nums)
5        prefix = [0]
6        for x in nums:
7            prefix.append(prefix[-1] + x)
8
9        groups = [[] for _ in range(k)]
10        groups[0].append(0)
11        best = None
12
13        for i in range(1, n + 1):
14            r = i % k
15            arr = groups[r]
16            pos = bisect.bisect_left(arr, prefix[i])
17            if pos < len(arr):
18                cand = prefix[i] - arr[0]
19                best = cand if best is None else max(best, cand)
20            else:
21                cand = prefix[i] - arr[0] if arr else None
22                if cand is not None:
23                    best = cand if best is None else max(best, cand)
24            bisect.insort(arr, prefix[i])
25
26        return 0 if best is None else best
27