class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1      # peak is on the right
            else:
                r = mid          # peak is here or on the left

        return l
