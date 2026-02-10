class Solution {
    public int numOfWays(int n) {
        long mod = 1000000007;
        long aba = 6;
        long abc = 6;
        for (int i = 2; i <= n; i++) {
            long newAba = (aba * 3 + abc * 2) % mod;
            long newAbc = (aba * 2 + abc * 2) % mod;
            aba = newAba;
            abc = newAbc;
        }
        return (int)((aba + abc) % mod);
    }
}
