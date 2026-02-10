class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        mp = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            mp[key].append(s)
        return list(mp.values())
