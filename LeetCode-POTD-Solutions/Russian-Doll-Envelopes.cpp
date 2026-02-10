1class Solution {
2public:
3    int maxEnvelopes(vector<vector<int>>& envelopes) {
4        if (envelopes.empty()) return 0;
5
6        // Step 1: Sort
7        sort(envelopes.begin(), envelopes.end(),
8             [](const vector<int>& a, const vector<int>& b) {
9                 if (a[0] == b[0])
10                     return a[1] > b[1]; // height descending if width same
11                 return a[0] < b[0];     // width ascending
12             });
13
14        // Step 2: LIS on heights
15        vector<int> lis;
16        for (auto& e : envelopes) {
17            int h = e[1];
18            auto it = lower_bound(lis.begin(), lis.end(), h);
19            if (it == lis.end())
20                lis.push_back(h);
21            else
22                *it = h;
23        }
24
25        return lis.size();
26    }
27};
28