1var countGoodStrings = function(low, high, zero, one) {
2    const MOD = 1e9 + 7;
3    const dp = new Array(high + 1).fill(0);
4
5    dp[0] = 1; // one way to build empty string
6
7    for (let i = 1; i <= high; i++) {
8        if (i - zero >= 0) {
9            dp[i] = (dp[i] + dp[i - zero]) % MOD;
10        }
11        if (i - one >= 0) {
12            dp[i] = (dp[i] + dp[i - one]) % MOD;
13        }
14    }
15
16    let result = 0;
17    for (let i = low; i <= high; i++) {
18        result = (result + dp[i]) % MOD;
19    }
20
21    return result;
22};
23