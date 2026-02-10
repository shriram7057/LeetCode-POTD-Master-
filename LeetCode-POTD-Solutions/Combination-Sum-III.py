class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, comb, total):
            if len(comb) == k:
                if total == n:
                    result.append(list(comb))
                return

            for num in range(start, 10):
                if total + num > n:
                    break
                comb.append(num)
                backtrack(num + 1, comb, total + num)
                comb.pop()

        backtrack(1, [], 0)
        return result
