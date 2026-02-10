class Solution {
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        int[][] row = new int[m + 1][n + 1];
        int[][] col = new int[m + 1][n + 1];
        int[][] diag1 = new int[m + 1][n + 1];
        int[][] diag2 = new int[m + 1][n + 2];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                row[i][j] = row[i][j - 1] + grid[i - 1][j - 1];
                col[i][j] = col[i - 1][j] + grid[i - 1][j - 1];
                diag1[i][j] = diag1[i - 1][j - 1] + grid[i - 1][j - 1];
                diag2[i][j] = diag2[i - 1][j + 1] + grid[i - 1][j - 1];
            }
        }

        for (int k = Math.min(m, n); k >= 2; k--) {
            for (int i = 1; i + k - 1 <= m; i++) {
                for (int j = 1; j + k - 1 <= n; j++) {
                    int s = row[i][j + k - 1] - row[i][j - 1];
                    boolean ok = true;

                    for (int r = i; r < i + k && ok; r++) {
                        if (row[r][j + k - 1] - row[r][j - 1] != s) ok = false;
                    }
                    for (int c = j; c < j + k && ok; c++) {
                        if (col[i + k - 1][c] - col[i - 1][c] != s) ok = false;
                    }
                    if (ok) {
                        int d1 = diag1[i + k - 1][j + k - 1] - diag1[i - 1][j - 1];
                        int d2 = diag2[i + k - 1][j] - diag2[i - 1][j + k];
                        if (d1 == s && d2 == s) return k;
                    }
                }
            }
        }
        return 1;
    }
}
