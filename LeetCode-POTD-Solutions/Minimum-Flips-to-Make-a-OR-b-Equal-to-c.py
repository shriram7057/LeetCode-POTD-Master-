class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0

        # Check all 32 bits
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1

            if bit_c == 1:
                # We need at least one of a or b to be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                # c bit is 0, so both a and b must be 0
                # count how many bits need flipping
                flips += bit_a + bit_b

        return flips
