class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        idx, step = 0, 1
        
        for c in s:
            rows[idx] += c
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        
        return "".join(rows)
