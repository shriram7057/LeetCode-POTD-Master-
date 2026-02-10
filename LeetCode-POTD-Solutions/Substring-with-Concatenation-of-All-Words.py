class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        wlen = len(words[0])
        total_len = wlen * len(words)
        count = {}
        
        for w in words:
            count[w] = count.get(w, 0) + 1
        
        res = []
        for i in range(wlen):
            l = i
            seen = {}
            for r in range(i, len(s) - wlen + 1, wlen):
                word = s[r:r + wlen]
                if word in count:
                    seen[word] = seen.get(word, 0) + 1
                    while seen[word] > count[word]:
                        seen[s[l:l + wlen]] -= 1
                        l += wlen
                    if r - l + wlen == total_len:
                        res.append(l)
                else:
                    seen.clear()
                    l = r + wlen
        
        return res
