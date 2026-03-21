class Solution {
public:
    vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
        int top = x;
        int bottom = x + k - 1;

        while (top < bottom) {
            for (int col = y; col < y + k; col++) {
                swap(grid[top][col], grid[bottom][col]);
            }
            top++;
            bottom--;
        }

        return grid;
    }
};
};