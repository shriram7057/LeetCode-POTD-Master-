1class Solution {
2public:
3    int searchInsert(vector<int>& nums, int target) {
4        int left = 0;
5        int right = nums.size() - 1;
6
7        while (left <= right) {
8            int mid = left + (right - left) / 2;
9
10            if (nums[mid] == target) {
11                return mid;
12            } else if (nums[mid] < target) {
13                left = mid + 1;
14            } else {
15                right = mid - 1;
16            }
17        }
18
19        // left is the correct insertion position
20        return left;
21    }
22};
23