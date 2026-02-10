1class Solution {
2public:
3    int minimumCost(vector<int>& nums) {
4        int n = nums.size();
5        int ans = INT_MAX;
6        for (int i = 1; i <= n - 2; i++) {
7            for (int j = i + 1; j <= n - 1; j++) {
8                ans = min(ans, nums[0] + nums[i] + nums[j]);
9            }
10        }
11        return ans;
12    }
13};
14