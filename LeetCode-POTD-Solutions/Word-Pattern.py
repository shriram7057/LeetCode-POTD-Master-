class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for p, w in zip(pattern, words):
            if p in p_to_w and p_to_w[p] != w:
                return False
            if w in w_to_p and w_to_p[w] != p:
                return False
            p_to_w[p] = w
            w_to_p[w] = p

        return True
