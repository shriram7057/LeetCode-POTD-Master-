1class Solution {
2public:
3    int dfs(int node, vector<vector<int>>& tree, vector<int>& informTime) {
4        int maxSubTime = 0;
5        for (int sub : tree[node]) {
6            maxSubTime = max(maxSubTime, dfs(sub, tree, informTime));
7        }
8        return informTime[node] + maxSubTime;
9    }
10
11    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
12        vector<vector<int>> tree(n);
13
14        // Build manager -> subordinates tree
15        for (int i = 0; i < n; i++) {
16            if (manager[i] != -1) {
17                tree[manager[i]].push_back(i);
18            }
19        }
20
21        return dfs(headID, tree, informTime);
22    }
23};
24