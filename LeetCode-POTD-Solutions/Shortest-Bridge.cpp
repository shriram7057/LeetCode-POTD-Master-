1class Solution {
2public:
3    int n;
4    vector<vector<int>> dirs{{1,0},{-1,0},{0,1},{0,-1}};
5    queue<pair<int,int>> q;
6
7    void dfs(int i, int j, vector<vector<int>>& grid) {
8        if (i < 0 || j < 0 || i >= n || j >= n || grid[i][j] != 1)
9            return;
10
11        grid[i][j] = 2;          // mark visited
12        q.push({i, j});          // add to BFS queue
13
14        for (auto& d : dirs)
15            dfs(i + d[0], j + d[1], grid);
16    }
17
18    int shortestBridge(vector<vector<int>>& grid) {
19        n = grid.size();
20        bool found = false;
21
22        // 1️⃣ Find first island
23        for (int i = 0; i < n && !found; i++) {
24            for (int j = 0; j < n && !found; j++) {
25                if (grid[i][j] == 1) {
26                    dfs(i, j, grid);
27                    found = true;
28                }
29            }
30        }
31
32        // 2️⃣ BFS to reach second island
33        int steps = 0;
34        while (!q.empty()) {
35            int size = q.size();
36            while (size--) {
37                auto [x, y] = q.front();
38                q.pop();
39
40                for (auto& d : dirs) {
41                    int nx = x + d[0], ny = y + d[1];
42                    if (nx < 0 || ny < 0 || nx >= n || ny >= n)
43                        continue;
44
45                    if (grid[nx][ny] == 1)
46                        return steps;   // reached second island
47
48                    if (grid[nx][ny] == 0) {
49                        grid[nx][ny] = 2;
50                        q.push({nx, ny});
51                    }
52                }
53            }
54            steps++;
55        }
56        return -1;
57    }
58};
59