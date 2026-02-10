class Solution {
    public int maxOperations(String s) {
        long operations = 0;
        long ones = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '1') {
                ones++;
            } else { // c == '0'
                // Only add operations if the next character is '1' or we're at the end
                if (i == n - 1 || s.charAt(i + 1) == '1') {
                    operations += ones;
                }
            }
        }

        return (int) operations;
    }
}
