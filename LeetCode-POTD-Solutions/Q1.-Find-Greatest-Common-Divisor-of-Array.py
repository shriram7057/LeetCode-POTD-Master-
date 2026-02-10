class Solution(object):
    def findGCD(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        mn = min(nums)
        mx = max(nums)
        return gcd(mn, mx)
