class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}

        # Count frequency of each number
        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        # Check if all frequencies are unique
        occurrences = freq.values()
        return len(occurrences) == len(set(occurrences))
