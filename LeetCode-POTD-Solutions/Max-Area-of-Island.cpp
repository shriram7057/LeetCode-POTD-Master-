1class Solution {
2public:
3    int m, n;
4
5    int dfs(vector<vector<int>>& grid, int r, int c) {
6        if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == 0)
7            return 0;
8
9        grid[r][c] = 0;  // mark visited
10        int area = 1;
11
12        area += dfs(grid, r + 1, c);
13        area += dfs(grid, r - 1, c);
14        area += dfs(grid, r, c + 1);
15        area += dfs(grid, r, c - 1);
16
17        return area;
18    }
19
20    int maxAreaOfIsland(vector<vector<int>>& grid) {
21        m = grid.size();
22        n = grid[0].size();
23        int maxArea = 0;
24
25        for (int i = 0; i < m; i++) {
26            for (int j = 0; j < n; j++) {
27                if (grid[i][j] == 1) {
28                    maxArea = max(maxArea, dfs(grid, i, j));
29                }
30            }
31        }
32
33        return maxArea;
34    }
35};
36