class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        const int MOD = 1e9 + 7;

        static int dp[201][201][2][201];
        memset(dp, 0, sizeof(dp));

        if (zero > 0) dp[1][0][0][1] = 1;
        if (one > 0) dp[0][1][1][1] = 1;

        for (int z = 0; z <= zero; z++) {
            for (int o = 0; o <= one; o++) {
                for (int last = 0; last < 2; last++) {
                    for (int len = 1; len <= limit; len++) {

                        int cur = dp[z][o][last][len];
                        if (!cur) continue;

                        if (last == 0) {
                            if (z + 1 <= zero && len + 1 <= limit)
                                dp[z+1][o][0][len+1] = (dp[z+1][o][0][len+1] + cur) % MOD;

                            if (o + 1 <= one)
                                dp[z][o+1][1][1] = (dp[z][o+1][1][1] + cur) % MOD;
                        }
                        else {
                            if (o + 1 <= one && len + 1 <= limit)
                                dp[z][o+1][1][len+1] = (dp[z][o+1][1][len+1] + cur) % MOD;

                            if (z + 1 <= zero)
                                dp[z+1][o][0][1] = (dp[z+1][o][0][1] + cur) % MOD;
                        }
                    }
                }
            }
        }

        long long ans = 0;

        for (int len = 1; len <= limit; len++) {
            ans = (ans + dp[zero][one][0][len]) % MOD;
            ans = (ans + dp[zero][one][1][len]) % MOD;
        }

        return ans;
    }
};