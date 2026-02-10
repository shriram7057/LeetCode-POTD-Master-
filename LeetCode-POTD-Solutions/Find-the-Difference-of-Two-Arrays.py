class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1 = set(nums1)
        s2 = set(nums2)

        return [
            list(s1 - s2),   # elements in nums1 not in nums2
            list(s2 - s1)    # elements in nums2 not in nums1
        ]
