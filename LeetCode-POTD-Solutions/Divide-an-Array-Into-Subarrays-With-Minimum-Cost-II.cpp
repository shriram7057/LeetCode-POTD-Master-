1#include <bits/stdc++.h>
2using namespace std;
3
4class Solution {
5public:
6    long long minimumCost(vector<int>& nums, int k, int dist) {
7        int n = nums.size();
8        long long ans = LLONG_MAX;
9
10        multiset<long long> small, large;
11        long long sumSmall = 0;
12
13        auto add = [&](long long x) {
14            small.insert(x);
15            sumSmall += x;
16            if ((int)small.size() > k - 1) {
17                auto it = prev(small.end());
18                sumSmall -= *it;
19                large.insert(*it);
20                small.erase(it);
21            }
22        };
23
24        auto remove = [&](long long x) {
25            auto it = small.find(x);
26            if (it != small.end()) {
27                sumSmall -= x;
28                small.erase(it);
29                if (!large.empty()) {
30                    auto it2 = large.begin();
31                    sumSmall += *it2;
32                    small.insert(*it2);
33                    large.erase(it2);
34                }
35            } else {
36                large.erase(large.find(x));
37            }
38        };
39
40        int left = 1;
41
42        for (int i = 1; i <= dist + 1 && i < n; i++) {
43            add(nums[i]);
44        }
45
46        for (int i = 1; i < n; i++) {
47            if ((int)small.size() == k - 1) {
48                ans = min(ans, nums[0] + sumSmall);
49            }
50
51            if (i + dist + 1 < n) {
52                add(nums[i + dist + 1]);
53            }
54
55            remove(nums[i]);
56        }
57
58        return ans;
59    }
60};
61