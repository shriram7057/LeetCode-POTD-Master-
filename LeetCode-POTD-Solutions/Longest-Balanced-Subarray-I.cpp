1class Solution {
2public:
3    int longestBalanced(vector<int>& nums) {
4        int n = nums.size();
5        int ans = 0;
6
7        for (int i = 0; i < n; i++) {
8            unordered_set<int> evenSet, oddSet;
9
10            for (int j = i; j < n; j++) {
11                if (nums[j] % 2 == 0) {
12                    evenSet.insert(nums[j]);
13                } else {
14                    oddSet.insert(nums[j]);
15                }
16
17                if (evenSet.size() == oddSet.size()) {
18                    ans = max(ans, j - i + 1);
19                }
20            }
21        }
22
23        return ans;
24    }
25};