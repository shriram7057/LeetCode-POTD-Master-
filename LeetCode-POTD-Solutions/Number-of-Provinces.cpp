1class Solution {
2public:
3    void dfs(int city, vector<vector<int>>& isConnected, vector<bool>& visited) {
4        visited[city] = true;
5        for (int next = 0; next < isConnected.size(); next++) {
6            if (isConnected[city][next] == 1 && !visited[next]) {
7                dfs(next, isConnected, visited);
8            }
9        }
10    }
11
12    int findCircleNum(vector<vector<int>>& isConnected) {
13        int n = isConnected.size();
14        vector<bool> visited(n, false);
15        int provinces = 0;
16
17        for (int i = 0; i < n; i++) {
18            if (!visited[i]) {
19                dfs(i, isConnected, visited);
20                provinces++;
21            }
22        }
23
24        return provinces;
25    }
26};
27