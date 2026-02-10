class Solution(object):
    def numberOfSubstrings(self, s):
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # shrink window while contains all 'a', 'b', 'c'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res
