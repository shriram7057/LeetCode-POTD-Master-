class Solution(object):
    def findKthNumber(self, n, k):

        def count_steps(n, a, b):
            steps = 0
            while a <= n:
                steps += min(n + 1, b) - a
                a *= 10
                b *= 10
            return steps

        cur = 1
        k -= 1

        while k > 0:
            steps = count_steps(n, cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1

        return cur
