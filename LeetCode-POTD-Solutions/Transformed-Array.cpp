1class Solution {
2public:
3    vector<int> constructTransformedArray(vector<int>& nums) {
4        int n = nums.size();
5        vector<int> result(n);
6
7        for (int i = 0; i < n; i++) {
8            if (nums[i] == 0) {
9                result[i] = 0;
10            } else {
11                int newIndex = (i + nums[i]) % n;
12                if (newIndex < 0) newIndex += n;  // handle negative modulo
13                result[i] = nums[newIndex];
14            }
15        }
16        return result;
17    }
18};
19