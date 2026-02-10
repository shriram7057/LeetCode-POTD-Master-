1class Solution {
2public:
3    int m, n;
4    vector<vector<int>> dirs{{1,0},{-1,0},{0,1},{0,-1}};
5
6    void dfs(int r, int c, vector<vector<int>>& heights, vector<vector<bool>>& ocean) {
7        ocean[r][c] = true;
8
9        for (auto& d : dirs) {
10            int nr = r + d[0], nc = c + d[1];
11            if (nr < 0 || nc < 0 || nr >= m || nc >= n)
12                continue;
13            if (ocean[nr][nc])
14                continue;
15            if (heights[nr][nc] < heights[r][c])
16                continue;
17
18            dfs(nr, nc, heights, ocean);
19        }
20    }
21
22    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
23        m = heights.size();
24        n = heights[0].size();
25
26        vector<vector<bool>> pacific(m, vector<bool>(n, false));
27        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
28
29        // Pacific: top row + left column
30        for (int i = 0; i < m; i++)
31            dfs(i, 0, heights, pacific);
32        for (int j = 0; j < n; j++)
33            dfs(0, j, heights, pacific);
34
35        // Atlantic: bottom row + right column
36        for (int i = 0; i < m; i++)
37            dfs(i, n - 1, heights, atlantic);
38        for (int j = 0; j < n; j++)
39            dfs(m - 1, j, heights, atlantic);
40
41        // Cells reachable by both
42        vector<vector<int>> res;
43        for (int i = 0; i < m; i++) {
44            for (int j = 0; j < n; j++) {
45                if (pacific[i][j] && atlantic[i][j]) {
46                    res.push_back({i, j});
47                }
48            }
49        }
50
51        return res;
52    }
53};
54