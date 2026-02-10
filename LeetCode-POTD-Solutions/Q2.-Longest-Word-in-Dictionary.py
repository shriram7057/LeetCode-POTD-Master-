class Solution(object):
    def longestWord(self, words):
        words.sort()
        good = set([""])
        ans = ""

        for w in words:
            if w[:-1] in good:
                good.add(w)
                if len(w) > len(ans):
                    ans = w

        return ans
