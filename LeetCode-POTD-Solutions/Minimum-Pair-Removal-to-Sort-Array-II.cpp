1class Solution {
2public:
3    using ll = long long;
4
5    int minimumPairRemoval(vector<int>& nums) {
6        int n = nums.size();
7        if (n <= 1)
8            return 0;
9
10        vector<ll> arr(nums.begin(), nums.end());
11        vector<bool> removed(n, false);
12        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
13
14        int sorted = 0;
15        for (int i = 1; i < n; ++i) {
16            pq.emplace(arr[i - 1] + arr[i], i - 1);
17            if (arr[i] >= arr[i - 1])
18                sorted++;
19        }
20        if (sorted == n - 1)
21            return 0;
22
23        int rem = n;
24        vector<int> prev(n), next(n);
25        for (int i = 0; i < n; ++i) {
26            prev[i] = i - 1;
27            next[i] = i + 1;
28        }
29
30        while (rem > 1) {
31            auto [sum, left] = pq.top();
32            pq.pop();
33            int right = next[left];
34            if (right >= n || removed[left] || removed[right] ||
35                arr[left] + arr[right] != sum)
36                continue;
37
38            int pre = prev[left];
39            int nxt = next[right];
40
41            if (arr[left] <= arr[right])
42                sorted--;
43            if (pre != -1 && arr[pre] <= arr[left])
44                sorted--;
45            if (nxt != n && arr[right] <= arr[nxt])
46                sorted--;
47
48            arr[left] += arr[right];
49            removed[right] = true;
50            rem--;
51
52            if (pre == -1) {
53                prev[left] = -1;
54            } else {
55                pq.emplace(arr[pre] + arr[left], pre);
56                if (arr[pre] <= arr[left])
57                    sorted++;
58            }
59
60            if (nxt == n) {
61                next[left] = n;
62            } else {
63                prev[nxt] = left;
64                next[left] = nxt;
65                pq.emplace(arr[left] + arr[nxt], left);
66                if (arr[left] <= arr[nxt])
67                    sorted++;
68            }
69
70            if (sorted == rem - 1)
71                return n - rem;
72        }
73        return n;
74    }
75};
76