class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            s = 0
            while n > 0:
                d = n % 10
                s += d * d
                n //= 10
            if s == 1:
                return True
            n = s
        return False
