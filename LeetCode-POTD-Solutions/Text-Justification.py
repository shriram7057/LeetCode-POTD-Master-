class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        
        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            spaces = maxWidth - sum(len(w) for w in line_words)
            gaps = len(line_words) - 1
            
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                space_each = spaces // gaps
                extra = spaces % gaps
                line = ""
                for k in range(gaps):
                    line += line_words[k] + " " * (space_each + (1 if k < extra else 0))
                line += line_words[-1]
            
            res.append(line)
            i = j
        
        return res
