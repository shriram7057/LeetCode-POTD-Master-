class Solution(object):
    def minSubarray(self, nums, p):
        need = sum(nums) % p
        if need == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        res = len(nums)

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            target = (prefix - need) % p

            if target in seen:
                res = min(res, i - seen[target])

            seen[prefix] = i

        return res if res < len(nums) else -1
