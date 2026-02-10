class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # If concatenating in both orders isn't the same,
        # there is no valid gcd string.
        if str1 + str2 != str2 + str1:
            return ""

        # Function to compute gcd of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Length of gcd determines the gcd string
        length = gcd(len(str1), len(str2))
        return str1[:length]
