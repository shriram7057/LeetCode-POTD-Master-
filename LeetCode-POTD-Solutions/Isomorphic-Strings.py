class Solution(object):
    def isIsomorphic(self, s, t):
        m1 = {}
        m2 = {}
        for a, b in zip(s, t):
            if (a in m1 and m1[a] != b) or (b in m2 and m2[b] != a):
                return False
            m1[a] = b
            m2[b] = a
        return True
