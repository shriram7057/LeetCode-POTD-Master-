class Solution {
    public long maxMatrixSum(int[][] matrix) {
        long sum = 0;
        int neg = 0;
        int minAbs = Integer.MAX_VALUE;

        for (int[] row : matrix) {
            for (int x : row) {
                if (x < 0) neg++;
                int a = Math.abs(x);
                sum += a;
                minAbs = Math.min(minAbs, a);
            }
        }

        if (neg % 2 == 1) sum -= 2L * minAbs;
        return sum;
    }
}
