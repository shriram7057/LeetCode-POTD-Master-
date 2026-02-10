class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = 1
        result = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        return result + sign * num
