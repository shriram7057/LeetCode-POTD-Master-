1class Solution {
2public:
3    bool canReach(vector<int>& arr, int start) {
4        int n = arr.size();
5        vector<bool> visited(n, false);
6        return dfs(arr, start, visited);
7    }
8
9private:
10    bool dfs(vector<int>& arr, int i, vector<bool>& visited) {
11        // Out of bounds or already visited
12        if (i < 0 || i >= arr.size() || visited[i]) {
13            return false;
14        }
15
16        // Found a zero
17        if (arr[i] == 0) {
18            return true;
19        }
20
21        visited[i] = true;
22
23        // Try both possible jumps
24        return dfs(arr, i + arr[i], visited) ||
25               dfs(arr, i - arr[i], visited);
26    }
27};
28