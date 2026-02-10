class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        ops = 0

        for n in nums:
            need = k - n
            if need in count and count[need] > 0:
                ops += 1
                count[need] -= 1
            else:
                count[n] = count.get(n, 0) + 1

        return ops
