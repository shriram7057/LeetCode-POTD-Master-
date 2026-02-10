class Solution(object):
    def countPalindromicSubsequence(self, s):
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        ans = 0
        for c in first:
            if first[c] < last[c]:
                ans += len(set(s[first[c] + 1:last[c]]))
        return ans
