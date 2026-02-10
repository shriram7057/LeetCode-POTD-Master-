class Solution(object):
    def decodeString(self, s):
        num = 0
        curr = ""
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)     # build full number
            elif ch == "[":
                stack.append((curr, num))    # push current string & number
                curr = ""                    # reset current string
                num = 0
            elif ch == "]":
                prev, k = stack.pop()        # pop previous string & repeat count
                curr = prev + curr * k       # expand
            else:
                curr += ch                   # normal letters go directly

        return curr
