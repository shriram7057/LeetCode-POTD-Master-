class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        return len(s.split()[-1])
