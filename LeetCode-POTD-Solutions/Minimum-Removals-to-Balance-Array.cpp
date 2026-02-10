1class Solution {
2public:
3    int minRemoval(vector<int>& nums, int k) {
4        sort(nums.begin(), nums.end());
5        
6        int n = nums.size();
7        int l = 0;
8        int maxLen = 1;
9        
10        for (int r = 0; r < n; r++) {
11            while ((long long)nums[r] > (long long)nums[l] * k) {
12                l++;
13            }
14            maxLen = max(maxLen, r - l + 1);
15        }
16        
17        return n - maxLen;
18    }
19};