class Solution(object):
    def longestPrefix(self, s):
        n = len(s)
        lps = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j

        # lps[-1] gives the length of longest prefix which is also suffix
        return s[:lps[-1]]
