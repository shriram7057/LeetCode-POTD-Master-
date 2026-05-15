class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Minimum is in right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // Minimum is at mid or in left half
            else {
                right = mid;
            }
        }

        return nums[left];
    }
}