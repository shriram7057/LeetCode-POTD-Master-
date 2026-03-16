class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        set<int> sums;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {

                // radius 0 rhombus
                sums.insert(grid[r][c]);

                for (int k = 1; ; k++) {
                    if (r-k < 0 || r+k >= m || c-k < 0 || c+k >= n) break;

                    int sum = 0;

                    int x = r-k, y = c;

                    // top -> right
                    for (int i = 0; i < k; i++)
                        sum += grid[x+i][y+i];

                    // right -> bottom
                    for (int i = 0; i < k; i++)
                        sum += grid[r+i][c+k-i];

                    // bottom -> left
                    for (int i = 0; i < k; i++)
                        sum += grid[r+k-i][c-i];

                    // left -> top
                    for (int i = 0; i < k; i++)
                        sum += grid[r-i][c-k+i];

                    sums.insert(sum);
                }
            }
        }

        vector<int> res;
        for (auto it = sums.rbegin(); it != sums.rend() && res.size() < 3; it++)
            res.push_back(*it);

        return res;
    }
};