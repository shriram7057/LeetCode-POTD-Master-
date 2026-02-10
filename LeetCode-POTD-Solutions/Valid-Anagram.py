class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1
        for c in t:
            idx = ord(c) - 97
            count[idx] -= 1
            if count[idx] < 0:
                return False
        return True
