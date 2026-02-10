1class Solution {
2public:
3    int countNegatives(vector<vector<int>>& grid) {
4        int m = grid.size();
5        int n = grid[0].size();
6
7        int row = 0;
8        int col = n - 1;
9        int count = 0;
10
11        while (row < m && col >= 0) {
12            if (grid[row][col] < 0) {
13                count += (m - row);
14                col--;
15            } else {
16                row++;
17            }
18        }
19
20        return count;
21    }
22};
23