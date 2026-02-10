1class Solution {
2public:
3    int largestPathValue(string colors, vector<vector<int>>& edges) {
4        int n = colors.size();
5        vector<vector<int>> graph(n);
6        vector<int> indegree(n, 0);
7
8        for (auto &e : edges) {
9            graph[e[0]].push_back(e[1]);
10            indegree[e[1]]++;
11        }
12
13        // dp[node][color]
14        vector<vector<int>> dp(n, vector<int>(26, 0));
15
16        queue<int> q;
17        for (int i = 0; i < n; i++) {
18            if (indegree[i] == 0) {
19                q.push(i);
20                dp[i][colors[i] - 'a'] = 1;
21            }
22        }
23
24        int visited = 0;
25        int ans = 0;
26
27        while (!q.empty()) {
28            int u = q.front();
29            q.pop();
30            visited++;
31
32            for (int c = 0; c < 26; c++)
33                ans = max(ans, dp[u][c]);
34
35            for (int v : graph[u]) {
36                for (int c = 0; c < 26; c++) {
37                    dp[v][c] = max(
38                        dp[v][c],
39                        dp[u][c] + (colors[v] - 'a' == c)
40                    );
41                }
42
43                if (--indegree[v] == 0)
44                    q.push(v);
45            }
46        }
47
48        return visited == n ? ans : -1;
49    }
50};
51