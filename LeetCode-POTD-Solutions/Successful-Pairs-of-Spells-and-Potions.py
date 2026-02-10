class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)
        result = []

        import bisect
        
        for s in spells:
            # Minimum potion value needed to reach success
            need = (success + s - 1) // s     # ceiling(success / s)

            # Find first position where potion >= need
            idx = bisect.bisect_left(potions, need)

            # Count of successful potions
            result.append(n - idx)

        return result
