class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]
        for i in range(1, len(words)):
            # Compare sorted characters of current and previous kept word
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        return result
