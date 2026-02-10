1class Solution {
2public:
3    int dfs(int node, int parent, vector<vector<pair<int,int>>>& graph) {
4        int changes = 0;
5
6        for (auto& [next, cost] : graph[node]) {
7            if (next == parent) continue;
8            changes += cost;
9            changes += dfs(next, node, graph);
10        }
11
12        return changes;
13    }
14
15    int minReorder(int n, vector<vector<int>>& connections) {
16        vector<vector<pair<int,int>>> graph(n);
17
18        for (auto& c : connections) {
19            int a = c[0], b = c[1];
20            graph[a].push_back({b, 1}); // original direction, needs change
21            graph[b].push_back({a, 0}); // reverse direction, already fine
22        }
23
24        return dfs(0, -1, graph);
25    }
26};
27