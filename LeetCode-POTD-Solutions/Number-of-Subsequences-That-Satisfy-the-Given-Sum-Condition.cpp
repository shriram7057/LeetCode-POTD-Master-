1class Solution {
2public:
3    int numSubseq(vector<int>& nums, int target) {
4        const int MOD = 1e9 + 7;
5        int n = nums.size();
6        sort(nums.begin(), nums.end());
7
8        vector<int> pow2(n + 1, 1);
9        for (int i = 1; i <= n; i++) {
10            pow2[i] = (pow2[i - 1] * 2) % MOD;
11        }
12
13        int left = 0, right = n - 1;
14        long long res = 0;
15
16        while (left <= right) {
17            if (nums[left] + nums[right] <= target) {
18                res = (res + pow2[right - left]) % MOD;
19                left++;
20            } else {
21                right--;
22            }
23        }
24
25        return (int)res;
26    }
27};
28