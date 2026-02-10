1class Solution {
2    public int search(int[] nums, int target) {
3        int left = 0, right = nums.length - 1;
4
5        while (left <= right) {
6            int mid = left + (right - left) / 2;
7
8            if (nums[mid] == target) return mid;
9
10            // Left half is sorted
11            if (nums[left] <= nums[mid]) {
12                if (nums[left] <= target && target < nums[mid]) {
13                    right = mid - 1;
14                } else {
15                    left = mid + 1;
16                }
17            }
18            // Right half is sorted
19            else {
20                if (nums[mid] < target && target <= nums[right]) {
21                    left = mid + 1;
22                } else {
23                    right = mid - 1;
24                }
25            }
26        }
27        return -1;
28    }
29}
30