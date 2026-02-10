class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = {}
        needCount = len(t)
        l = 0
        res = ""
        minLen = float('inf')
        
        for r, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            if need.get(c, 0) >= have[c]:
                needCount -= 1
            
            while needCount == 0:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]
                have[s[l]] -= 1
                if need.get(s[l], 0) > have[s[l]]:
                    needCount += 1
                l += 1
        
        return res
