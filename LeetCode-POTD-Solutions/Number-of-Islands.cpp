1class Solution {
2public:
3    int m, n;
4    
5    void dfs(vector<vector<char>>& grid, int r, int c) {
6        // boundary + water check
7        if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == '0')
8            return;
9        
10        // mark current land as visited
11        grid[r][c] = '0';
12        
13        // explore all 4 directions
14        dfs(grid, r + 1, c);
15        dfs(grid, r - 1, c);
16        dfs(grid, r, c + 1);
17        dfs(grid, r, c - 1);
18    }
19    
20    int numIslands(vector<vector<char>>& grid) {
21        if (grid.empty()) return 0;
22        
23        m = grid.size();
24        n = grid[0].size();
25        int islands = 0;
26        
27        for (int i = 0; i < m; i++) {
28            for (int j = 0; j < n; j++) {
29                if (grid[i][j] == '1') {
30                    islands++;
31                    dfs(grid, i, j);
32                }
33            }
34        }
35        
36        return islands;
37    }
38};
39