1class Solution {
2public:
3    vector<int> searchRange(vector<int>& nums, int target) {
4        return {findFirst(nums, target), findLast(nums, target)};
5    }
6
7private:
8    int findFirst(vector<int>& nums, int target) {
9        int left = 0, right = nums.size() - 1;
10        int ans = -1;
11
12        while (left <= right) {
13            int mid = left + (right - left) / 2;
14
15            if (nums[mid] >= target) {
16                if (nums[mid] == target) ans = mid;
17                right = mid - 1;
18            } else {
19                left = mid + 1;
20            }
21        }
22        return ans;
23    }
24
25    int findLast(vector<int>& nums, int target) {
26        int left = 0, right = nums.size() - 1;
27        int ans = -1;
28
29        while (left <= right) {
30            int mid = left + (right - left) / 2;
31
32            if (nums[mid] <= target) {
33                if (nums[mid] == target) ans = mid;
34                left = mid + 1;
35            } else {
36                right = mid - 1;
37            }
38        }
39        return ans;
40    }
41};
42