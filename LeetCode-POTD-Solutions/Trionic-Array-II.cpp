1class Solution {
2public:
3    long long maxSumTrionic(vector<int>& nums) {
4        int n = nums.size();
5        const long long NEG = LLONG_MIN / 4;
6
7        long long inc1 = NEG;  // first increasing
8        long long dec  = NEG;  // increasing → decreasing
9        long long inc2 = NEG;  // trionic
10
11        long long ans = NEG;
12
13        for (int i = 1; i < n; i++) {
14            long long new_inc1 = NEG, new_dec = NEG, new_inc2 = NEG;
15
16            // first increasing
17            if (nums[i] > nums[i - 1]) {
18                new_inc1 = max(inc1 + nums[i],
19                               (long long)nums[i - 1] + nums[i]);
20            }
21
22            // decreasing
23            if (nums[i] < nums[i - 1]) {
24                new_dec = max(dec + nums[i],
25                              inc1 + nums[i]);
26            }
27
28            // second increasing
29            if (nums[i] > nums[i - 1]) {
30                new_inc2 = max(inc2 + nums[i],
31                               dec + nums[i]);
32            }
33
34            inc1 = new_inc1;
35            dec  = new_dec;
36            inc2 = new_inc2;
37
38            ans = max(ans, inc2);
39        }
40
41        return ans;
42    }
43};
44