class Solution(object):
    def sumScores(self, s):
        n = len(s)
        Z = [0] * n
        
        # Z-algorithm
        l = r = 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l = i
                r = i + Z[i] - 1

        # Sum of scores = sum(Z) + n (full match at index 0)
        return sum(Z) + n
