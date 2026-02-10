1class Solution {
2public:
3    int m, n;
4    
5    void dfs(vector<vector<int>>& grid, int r, int c) {
6        if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == 0)
7            return;
8        
9        grid[r][c] = 0;  // remove land
10        
11        dfs(grid, r + 1, c);
12        dfs(grid, r - 1, c);
13        dfs(grid, r, c + 1);
14        dfs(grid, r, c - 1);
15    }
16    
17    int numEnclaves(vector<vector<int>>& grid) {
18        m = grid.size();
19        n = grid[0].size();
20        
21        // 1️⃣ Remove all land connected to boundaries
22        for (int i = 0; i < m; i++) {
23            dfs(grid, i, 0);
24            dfs(grid, i, n - 1);
25        }
26        
27        for (int j = 0; j < n; j++) {
28            dfs(grid, 0, j);
29            dfs(grid, m - 1, j);
30        }
31        
32        // 2️⃣ Count remaining land cells
33        int count = 0;
34        for (int i = 0; i < m; i++) {
35            for (int j = 0; j < n; j++) {
36                if (grid[i][j] == 1)
37                    count++;
38            }
39        }
40        
41        return count;
42    }
43};
44