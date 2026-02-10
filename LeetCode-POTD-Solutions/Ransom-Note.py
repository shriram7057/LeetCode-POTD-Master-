class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = [0] * 26
        for c in magazine:
            freq[ord(c) - 97] += 1
        for c in ransomNote:
            i = ord(c) - 97
            freq[i] -= 1
            if freq[i] < 0:
                return False
        return True
