class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != ch:
                    return ans
            ans += ch
        return ans
