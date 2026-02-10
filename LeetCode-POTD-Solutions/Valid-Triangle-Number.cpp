1class Solution {
2public:
3    int triangleNumber(vector<int>& nums) {
4        sort(nums.begin(), nums.end());
5        int n = nums.size();
6        int count = 0;
7
8        for (int i = n - 1; i >= 2; --i) {
9            int left = 0, right = i - 1;
10            while (left < right) {
11                if (nums[left] + nums[right] > nums[i]) {
12                    count += right - left;
13                    right--;
14                } else {
15                    left++;
16                }
17            }
18        }
19        return count;
20    }
21};
22