class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Minimum is in left half (including mid)
            if (nums[mid] < nums[right]) {
                right = mid;
            }
            // Minimum is in right half
            else if (nums[mid] > nums[right]) {
                left = mid + 1;
            }
            // Duplicates: cannot decide, shrink search space
            else {
                right--;
            }
        }

        return nums[left];
    }
}