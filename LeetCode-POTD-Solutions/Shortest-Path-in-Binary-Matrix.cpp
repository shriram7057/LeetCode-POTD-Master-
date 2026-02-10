1class Solution {
2public:
3    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
4        int n = grid.size();
5
6        // Edge cases
7        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1)
8            return -1;
9
10        // 8 directions (including diagonals)
11        vector<pair<int, int>> dirs = {
12            {1, 0}, {-1, 0}, {0, 1}, {0, -1},
13            {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
14        };
15
16        queue<pair<int, int>> q;
17        q.push({0, 0});
18        grid[0][0] = 1;  // mark visited
19        int pathLen = 1;
20
21        while (!q.empty()) {
22            int size = q.size();
23
24            while (size--) {
25                auto [r, c] = q.front();
26                q.pop();
27
28                // Reached destination
29                if (r == n - 1 && c == n - 1)
30                    return pathLen;
31
32                for (auto& d : dirs) {
33                    int nr = r + d.first;
34                    int nc = c + d.second;
35
36                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
37                        grid[nr][nc] = 1; // mark visited
38                        q.push({nr, nc});
39                    }
40                }
41            }
42
43            pathLen++;
44        }
45
46        return -1;
47    }
48};
49