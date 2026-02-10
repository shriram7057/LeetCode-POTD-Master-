1class Solution:
2    def guessNumber(self, n: int) -> int:
3        left, right = 1, n
4
5        while left <= right:
6            mid = left + (right - left) // 2
7            res = guess(mid)
8
9            if res == 0:
10                return mid
11            elif res < 0:
12                right = mid - 1
13            else:
14                left = mid + 1
15