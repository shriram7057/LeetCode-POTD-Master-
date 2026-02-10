class Solution {
    public int sumFourDivisors(int[] nums) {
        int res = 0;
        for (int x : nums) {
            int sum = 0, cnt = 0;
            for (int d = 1; d * d <= x; d++) {
                if (x % d == 0) {
                    int d2 = x / d;
                    cnt++;
                    sum += d;
                    if (d != d2) {
                        cnt++;
                        sum += d2;
                    }
                    if (cnt > 4) break;
                }
            }
            if (cnt == 4) res += x;
        }
        return res;
    }
}