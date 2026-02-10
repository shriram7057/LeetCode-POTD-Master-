class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter

        c1 = Counter(word1)
        c2 = Counter(word2)

        # Condition 1: both strings must use the same set of characters
        if set(c1.keys()) != set(c2.keys()):
            return False

        # Condition 2: the sorted frequencies must match
        return sorted(c1.values()) == sorted(c2.values())
