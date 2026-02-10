1class Solution {
2public:
3    int findNumberOfLIS(vector<int>& nums) {
4        int n = nums.size();
5        if (n == 0) return 0;
6
7        vector<int> len(n, 1);   // LIS length ending at i
8        vector<int> cnt(n, 1);   // number of LIS ending at i
9
10        int maxLen = 1;
11
12        for (int i = 0; i < n; i++) {
13            for (int j = 0; j < i; j++) {
14                if (nums[j] < nums[i]) {
15                    if (len[j] + 1 > len[i]) {
16                        len[i] = len[j] + 1;
17                        cnt[i] = cnt[j];
18                    } else if (len[j] + 1 == len[i]) {
19                        cnt[i] += cnt[j];
20                    }
21                }
22            }
23            maxLen = max(maxLen, len[i]);
24        }
25
26        int result = 0;
27        for (int i = 0; i < n; i++) {
28            if (len[i] == maxLen) {
29                result += cnt[i];
30            }
31        }
32
33        return result;
34    }
35};
36