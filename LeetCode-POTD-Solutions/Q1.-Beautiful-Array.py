class Solution(object):
    def beautifulArray(self, n):
        res = [1]

        while len(res) < n:
            odd = [x * 2 - 1 for x in res]
            even = [x * 2 for x in res]
            res = odd + even

        return [x for x in res if x <= n]
