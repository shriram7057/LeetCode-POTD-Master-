class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        int ones = 0;
        for (int num : nums) {
            if (num == 1) ones++;
        }
        // If there are already some 1s: every non-1 can become 1 in one operation each
        if (ones > 0) {
            return n - ones;
        }
        // Otherwise we need to first create a 1 by GCDing a subarray until GCD == 1
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int g = nums[i];
            if (g == 1) { // though we checked none are 1
                minLen = 1;
                break;
            }
            for (int j = i + 1; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    minLen = Math.min(minLen, j - i + 1);
                    break;
                }
            }
        }
        if (minLen == Integer.MAX_VALUE) {
            return -1;
        }
        // It takes (minLen - 1) operations to make one element 1,
        // and then (n - 1) more operations to turn rest into 1s using that 1
        return (minLen - 1) + (n - 1);
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
