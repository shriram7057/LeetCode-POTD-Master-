class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        
        // prefix sum in-place
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) grid[i][j] += grid[i-1][j];
                if (j > 0) grid[i][j] += grid[i][j-1];
                if (i > 0 && j > 0) grid[i][j] -= grid[i-1][j-1];
            }
        }
        
        int count = 0;
        
        // submatrices starting at (0,0)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] <= k) count++;
            }
        }
        
        return count;
    }
};