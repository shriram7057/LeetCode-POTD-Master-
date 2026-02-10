class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        mod = 10**9 + 7

        def kadane(a):
            best = 0
            cur = 0
            for x in a:
                cur = max(0, cur + x)
                best = max(best, cur)
            return best

        if k == 1:
            return kadane(arr) % mod

        total = sum(arr)
        best_two = kadane(arr + arr)

        if total > 0:
            return (best_two + (k - 2) * total) % mod
        else:
            return best_two % mod
