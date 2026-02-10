1class Solution(object):
2    def deleteAndEarn(self, nums):
3        if not nums:
4            return 0
5
6        # Step 1: Count total points for each number
7        from collections import Counter
8        count = Counter(nums)
9
10        # Step 2: Convert into a sorted list of unique numbers
11        unique_nums = sorted(count.keys())
12
13        # Step 3: Dynamic Programming like House Robber
14        prev = None
15        a = 0  # dp[i-2]
16        b = 0  # dp[i-1]
17
18        for num in unique_nums:
19            points = num * count[num]  # total points from choosing 'num'
20            
21            if prev == num - 1:
22                # Adjacent → cannot take both
23                c = max(b, a + points)
24            else:
25                # Not adjacent → free to take
26                c = b + points
27
28            a, b = b, c
29            prev = num
30
31        return b
32