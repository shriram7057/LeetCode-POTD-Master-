1from collections import deque
2
3class Solution(object):
4    def countPartitions(self, nums, k):
5        MOD = 10**9 + 7
6        n = len(nums)
7
8        dp = [0] * (n + 1)
9        pref = [0] * (n + 1)
10        dp[0] = 1
11        pref[0] = 1
12
13        minD = deque()
14        maxD = deque()
15        left = 0
16
17        for right in range(n):
18            # Maintain deques for min
19            while minD and minD[-1] > nums[right]:
20                minD.pop()
21            minD.append(nums[right])
22
23            # Maintain deques for max
24            while maxD and maxD[-1] < nums[right]:
25                maxD.pop()
26            maxD.append(nums[right])
27
28            # Shrink window until max-min <= k
29            while maxD[0] - minD[0] > k:
30                if minD[0] == nums[left]:
31                    minD.popleft()
32                if maxD[0] == nums[left]:
33                    maxD.popleft()
34                left += 1
35
36            # dp[right+1] = sum(dp[left], ..., dp[right])
37            dp[right+1] = (pref[right] - (pref[left-1] if left > 0 else 0)) % MOD
38
39            # Update prefix sums
40            pref[right+1] = (pref[right] + dp[right+1]) % MOD
41
42        return dp[n]
43