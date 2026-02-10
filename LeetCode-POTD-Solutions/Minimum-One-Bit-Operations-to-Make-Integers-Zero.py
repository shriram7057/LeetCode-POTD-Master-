class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Recursive Gray-code pattern:
        # f(0) = 0
        # f(n) = 2^k - 1 - f(n - 2^k), where k = highest bit of n
        if n == 0:
            return 0
        k = n.bit_length() - 1
        return (1 << (k + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << k))
