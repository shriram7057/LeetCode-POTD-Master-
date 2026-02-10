class Solution(object):
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(i, parts, curr):
            # If we have 4 parts and used up all chars
            if parts == 4 and i == len(s):
                res.append(curr[:-1])  # remove trailing dot
                return

            # If too many parts or no chars left but need more parts
            if parts == 4 or i == len(s):
                return

            # Try segments of length 1 to 3
            for l in range(1, 4):
                if i + l > len(s):
                    break
                part = s[i:i+l]

                # No leading zero, unless part == "0"
                if (part[0] == '0' and l > 1):
                    continue

                # Value must be <= 255
                if int(part) > 255:
                    continue

                backtrack(i + l, parts + 1, curr + part + ".")

        backtrack(0, 0, "")
        return res
