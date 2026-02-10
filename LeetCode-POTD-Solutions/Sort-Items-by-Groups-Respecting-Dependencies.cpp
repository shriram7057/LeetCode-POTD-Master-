1class Solution {
2public:
3    vector<int> topoSort(int n, vector<vector<int>>& graph, vector<int>& indegree) {
4        queue<int> q;
5        vector<int> res;
6
7        for (int i = 0; i < n; i++)
8            if (indegree[i] == 0)
9                q.push(i);
10
11        while (!q.empty()) {
12            int u = q.front(); q.pop();
13            res.push_back(u);
14            for (int v : graph[u]) {
15                if (--indegree[v] == 0)
16                    q.push(v);
17            }
18        }
19
20        return res.size() == n ? res : vector<int>{};
21    }
22
23    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
24        // Step 1: Assign unique groups to -1 items
25        int gid = m;
26        for (int i = 0; i < n; i++) {
27            if (group[i] == -1)
28                group[i] = gid++;
29        }
30
31        // Graphs
32        vector<vector<int>> itemGraph(n);
33        vector<int> itemIndegree(n, 0);
34
35        vector<vector<int>> groupGraph(gid);
36        vector<int> groupIndegree(gid, 0);
37
38        // Step 2: Build graphs
39        for (int i = 0; i < n; i++) {
40            for (int prev : beforeItems[i]) {
41                itemGraph[prev].push_back(i);
42                itemIndegree[i]++;
43
44                if (group[prev] != group[i]) {
45                    groupGraph[group[prev]].push_back(group[i]);
46                    groupIndegree[group[i]]++;
47                }
48            }
49        }
50
51        // Step 3: Topo sort
52        vector<int> itemOrder = topoSort(n, itemGraph, itemIndegree);
53        vector<int> groupOrder = topoSort(gid, groupGraph, groupIndegree);
54
55        if (itemOrder.empty() || groupOrder.empty())
56            return {};
57
58        // Step 4: Collect items per group
59        unordered_map<int, vector<int>> groupItems;
60        for (int item : itemOrder)
61            groupItems[group[item]].push_back(item);
62
63        // Step 5: Build answer
64        vector<int> result;
65        for (int g : groupOrder) {
66            for (int item : groupItems[g])
67                result.push_back(item);
68        }
69
70        return result;
71    }
72};
73