class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(s, open_p, close_p):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open_p < n:
                backtrack(s + "(", open_p + 1, close_p)
            if close_p < open_p:
                backtrack(s + ")", open_p, close_p + 1)

        backtrack("", 0, 0)
        return res
