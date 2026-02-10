class Solution(object):
    def partition(self, s):
        res = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start, path):
            if start == len(s):
                res.append(list(path))
                return
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return res
