1#include <bits/stdc++.h>
2using namespace std;
3
4class Solution {
5public:
6    long long minimumCost(string source, string target,
7                          vector<string>& original,
8                          vector<string>& changed,
9                          vector<int>& cost) {
10        const long long INF = LLONG_MAX / 4;
11        int n = source.size();
12
13        // Group rules by length
14        unordered_map<int, vector<int>> byLen;
15        for (int i = 0; i < original.size(); i++) {
16            byLen[original[i].size()].push_back(i);
17        }
18
19        // For each length L: map string -> id, run Floyd–Warshall
20        unordered_map<int, unordered_map<string, int>> id;
21        unordered_map<int, vector<vector<long long>>> dist;
22
23        for (auto &[L, ids] : byLen) {
24            unordered_map<string, int> mp;
25            for (int i : ids) {
26                if (!mp.count(original[i]))
27                    mp[original[i]] = mp.size();
28                if (!mp.count(changed[i]))
29                    mp[changed[i]] = mp.size();
30            }
31
32            int sz = mp.size();
33            vector<vector<long long>> d(sz, vector<long long>(sz, INF));
34            for (int i = 0; i < sz; i++) d[i][i] = 0;
35
36            for (int i : ids) {
37                int u = mp[original[i]];
38                int v = mp[changed[i]];
39                d[u][v] = min(d[u][v], (long long)cost[i]);
40            }
41
42            for (int k = 0; k < sz; k++)
43                for (int i = 0; i < sz; i++)
44                    for (int j = 0; j < sz; j++)
45                        if (d[i][k] + d[k][j] < d[i][j])
46                            d[i][j] = d[i][k] + d[k][j];
47
48            id[L] = move(mp);
49            dist[L] = move(d);
50        }
51
52        // DP
53        vector<long long> dp(n + 1, INF);
54        dp[0] = 0;
55
56        for (int i = 0; i < n; i++) {
57            if (dp[i] == INF) continue;
58
59            // Single character (no cost if equal)
60            if (source[i] == target[i])
61                dp[i + 1] = min(dp[i + 1], dp[i]);
62
63            // Substring conversions
64            for (auto &[L, mp] : id) {
65                if (i + L > n) continue;
66                string s1 = source.substr(i, L);
67                string s2 = target.substr(i, L);
68                if (!mp.count(s1) || !mp.count(s2)) continue;
69
70                int u = mp[s1], v = mp[s2];
71                long long d = dist[L][u][v];
72                if (d < INF)
73                    dp[i + L] = min(dp[i + L], dp[i] + d);
74            }
75        }
76
77        return dp[n] == INF ? -1 : dp[n];
78    }
79};
80