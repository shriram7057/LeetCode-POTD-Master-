class Solution(object):
    def shortestPalindrome(self, s):
        rev = s[::-1]
        combined = s + "#" + rev

        # Build LPS array (longest prefix suffix)
        lps = [0] * len(combined)
        j = 0

        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j

        # lps[-1] = longest palindromic prefix size
        longest = lps[-1]

        # Add reverse of the rest in front
        return rev[:len(s) - longest] + s
