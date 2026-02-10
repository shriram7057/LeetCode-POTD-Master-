class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        res = 0
        dec = 0
        for i in range(k):
            val = happiness[i] - dec
            if val <= 0:
                break
            res += val
            dec += 1
        return res
