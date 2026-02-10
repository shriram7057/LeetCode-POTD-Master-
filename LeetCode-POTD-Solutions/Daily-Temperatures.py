class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res
