class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        res = []
        pc = [0] * 26
        sc = [0] * 26
        
        for c in p:
            pc[ord(c) - 97] += 1
        
        for i in range(len(s)):
            sc[ord(s[i]) - 97] += 1
            
            if i >= len(p):
                sc[ord(s[i - len(p)]) - 97] -= 1
            
            if sc == pc:
                res.append(i - len(p) + 1)
        
        return res
