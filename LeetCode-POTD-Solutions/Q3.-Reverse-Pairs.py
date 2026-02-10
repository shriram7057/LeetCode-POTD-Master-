class Solution(object):
    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums)-1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        count = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid+1, r)

        # Count reverse pairs
        j = mid + 1
        for i in range(l, mid+1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)

        # Merge the two sorted halves
        temp = []
        i, j = l, mid + 1

        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= r:
            temp.append(nums[j])
            j += 1

        nums[l:r+1] = temp
        return count
