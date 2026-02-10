1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if not s:
4            return ""
5
6        start = end = 0
7
8        def expand(l, r):
9            while l >= 0 and r < len(s) and s[l] == s[r]:
10                l -= 1
11                r += 1
12            return r - l - 1  # length of palindrome
13
14        for i in range(len(s)):
15            len1 = expand(i, i)       # odd length
16            len2 = expand(i, i + 1)   # even length
17            max_len = max(len1, len2)
18
19            if max_len > end - start:
20                start = i - (max_len - 1) // 2
21                end = i + max_len // 2
22
23        return s[start:end + 1]
24