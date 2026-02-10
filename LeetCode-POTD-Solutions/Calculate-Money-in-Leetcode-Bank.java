class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int days = n % 7;
        int total = 0;

        // Sum for full weeks
        for (int i = 0; i < weeks; i++) {
            total += 28 + (i * 7);
        }

        // Sum for remaining days
        for (int i = 0; i < days; i++) {
            total += (weeks + 1) + i;
        }

        return total;
    }
}
