1class Solution {
2    public int findMin(int[] nums) {
3        int left = 0, right = nums.length - 1;
4
5        while (left < right) {
6            int mid = left + (right - left) / 2;
7
8            if (nums[mid] > nums[right]) {
9                left = mid + 1;
10            } 
11            else if (nums[mid] < nums[right]) {
12                right = mid;
13            } 
14            else { 
15                // nums[mid] == nums[right]
16                right--;
17            }
18        }
19        return nums[left];
20    }
21}
22