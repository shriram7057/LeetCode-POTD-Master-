1from collections import Counter
2
3class Solution(object):
4    def specialTriplets(self, nums):
5        MOD = 10**9 + 7
6        n = len(nums)
7        right = Counter(nums)
8        left = Counter()
9        ans = 0
10        for x in nums:
11            right[x] -= 1
12            two_x = x * 2
13            ans = (ans + left[two_x] * right[two_x]) % MOD
14            left[x] += 1
15        return ans
16