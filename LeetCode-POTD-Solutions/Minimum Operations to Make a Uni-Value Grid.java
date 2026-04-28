class Solution {
    public int minOperations(int[][] grid, int x) {
        int n = grid.length, m = grid[0].length;
        int N = n * m;
        int[] freq = new int[10001];
        int min = grid[0][0], max = min;

        for (int[] row : grid) {
            for (int c : row) {
                if ((c - grid[0][0]) % x != 0) return -1;
                freq[c]++;
                min = Math.min(min, c);
                max = Math.max(max, c);
            }
        }

        int target = (N + 1) / 2;
        int acc = 0, med = min;

        for (int i = min; i <= max; i += x) {
            acc += freq[i];
            if (acc >= target) {
                med = i;
                break;
            }
        }

        int ops = 0;
        for (int i = min; i <= max; i += x)
            ops += Math.abs(i - med) / x * freq[i];

        return ops;
    }
}