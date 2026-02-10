1class Solution(object):
2    def countOdds(self, low, high):
3        return ((high + 1) // 2) - (low // 2)
4