1class Solution {
2public:
3    vector<int> shortestAlternatingPaths(
4        int n,
5        vector<vector<int>>& redEdges,
6        vector<vector<int>>& blueEdges
7    ) {
8        vector<vector<int>> red(n), blue(n);
9
10        for (auto& e : redEdges) {
11            red[e[0]].push_back(e[1]);
12        }
13        for (auto& e : blueEdges) {
14            blue[e[0]].push_back(e[1]);
15        }
16
17        // dist[node][color]: shortest distance reaching node
18        // color = 0 (red), 1 (blue)
19        vector<vector<int>> dist(n, vector<int>(2, -1));
20        queue<pair<int, int>> q;
21
22        // Start from node 0 with both colors
23        dist[0][0] = dist[0][1] = 0;
24        q.push({0, 0});
25        q.push({0, 1});
26
27        while (!q.empty()) {
28            auto [node, lastColor] = q.front();
29            q.pop();
30
31            // If last edge was red, next must be blue
32            if (lastColor == 0) {
33                for (int next : blue[node]) {
34                    if (dist[next][1] == -1) {
35                        dist[next][1] = dist[node][0] + 1;
36                        q.push({next, 1});
37                    }
38                }
39            }
40            // If last edge was blue, next must be red
41            else {
42                for (int next : red[node]) {
43                    if (dist[next][0] == -1) {
44                        dist[next][0] = dist[node][1] + 1;
45                        q.push({next, 0});
46                    }
47                }
48            }
49        }
50
51        vector<int> ans(n);
52        for (int i = 0; i < n; i++) {
53            if (dist[i][0] == -1) ans[i] = dist[i][1];
54            else if (dist[i][1] == -1) ans[i] = dist[i][0];
55            else ans[i] = min(dist[i][0], dist[i][1]);
56        }
57
58        return ans;
59    }
60};
61