class Solution(object):
    def magicalString(self, n):
        if n == 0:
            return 0
        if n <= 3:
            return 1  # magical string starts with "122"

        s = [1, 2, 2]
        i = 2   # pointer to read how many times to append
        num = 1 # next number to append (alternate between 1 and 2)

        while len(s) < n:
            count = s[i]          # how many times to append num
            s.extend([num] * count)
            num = 3 - num         # swap: 1 -> 2, 2 -> 1
            i += 1

        return s[:n].count(1)
