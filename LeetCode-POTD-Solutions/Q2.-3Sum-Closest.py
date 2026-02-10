class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                # Update closest if this sum is closer
                if abs(s - target) < abs(closest - target):
                    closest = s

                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return closest
