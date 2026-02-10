1class Solution {
2public:
3    vector<vector<int>> graph;
4    vector<int> disc, low;
5    vector<vector<int>> bridges;
6    int time = 0;
7
8    void dfs(int u, int parent) {
9        disc[u] = low[u] = time++;
10
11        for (int v : graph[u]) {
12            if (v == parent) continue;
13
14            if (disc[v] == -1) {
15                dfs(v, u);
16                low[u] = min(low[u], low[v]);
17
18                // Bridge condition
19                if (low[v] > disc[u]) {
20                    bridges.push_back({u, v});
21                }
22            } else {
23                // Back edge
24                low[u] = min(low[u], disc[v]);
25            }
26        }
27    }
28
29    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
30        graph.resize(n);
31        disc.assign(n, -1);
32        low.assign(n, -1);
33
34        for (auto& e : connections) {
35            graph[e[0]].push_back(e[1]);
36            graph[e[1]].push_back(e[0]);
37        }
38
39        dfs(0, -1); // graph is connected
40
41        return bridges;
42    }
43};
44