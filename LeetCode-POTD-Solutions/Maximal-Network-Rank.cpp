1class Solution {
2public:
3    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
4        vector<int> degree(n, 0);
5        vector<vector<bool>> connected(n, vector<bool>(n, false));
6
7        for (auto& r : roads) {
8            int a = r[0], b = r[1];
9            degree[a]++;
10            degree[b]++;
11            connected[a][b] = true;
12            connected[b][a] = true;
13        }
14
15        int ans = 0;
16        for (int i = 0; i < n; i++) {
17            for (int j = i + 1; j < n; j++) {
18                int rank = degree[i] + degree[j];
19                if (connected[i][j]) rank--;
20                ans = max(ans, rank);
21            }
22        }
23
24        return ans;
25    }
26};
27