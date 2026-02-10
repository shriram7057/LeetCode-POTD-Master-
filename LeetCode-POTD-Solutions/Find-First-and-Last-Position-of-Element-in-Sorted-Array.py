class Solution:
    def searchRange(self, nums, target):
        def findLeft():
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx

        def findRight():
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    idx = mid
            return idx

        return [findLeft(), findRight()]
