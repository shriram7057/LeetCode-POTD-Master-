class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        length = 0
        
        for i in range(1, n + 1):
            # If i is a power of 2, increase bit length
            if (i & (i - 1)) == 0:
                length += 1
            
            # Shift left and add current number
            result = ((result << length) | i) % MOD
        
        return result