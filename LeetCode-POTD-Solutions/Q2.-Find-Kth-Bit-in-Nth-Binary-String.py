class Solution(object):
    def findKthBit(self, n, k):
        # length of Sn is 2^n - 1
        length = (1 << n) - 1
        
        # recursive helper
        def solve(n, k, length):
            if n == 1:
                return "0"
            
            mid = (length // 2) + 1
            
            if k == mid:                 # middle bit is always '1'
                return "1"
            elif k < mid:                # in S_(n-1)
                return solve(n - 1, k, length // 2)
            else:
                # reflected and inverted bit
                k_mirror = mid - (k - mid)
                bit = solve(n - 1, k_mirror, length // 2)
                return "1" if bit == "0" else "0"

        return solve(n, k, length)
