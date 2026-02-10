1class Solution(object):
2    def isOneBitCharacter(self, bits):
3        i = 0
4        while i < len(bits) - 1:
5            i += 2 if bits[i] == 1 else 1
6        return i == len(bits) - 1