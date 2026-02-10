1var numTilings = function(n) {
2    const MOD = 1e9 + 7;
3
4    if (n <= 2) return n;
5
6    let dp0 = 1; // dp[i-3]
7    let dp1 = 1; // dp[i-2]
8    let dp2 = 2; // dp[i-1]
9
10    for (let i = 3; i <= n; i++) {
11        let curr = (2 * dp2 + dp0) % MOD;
12        dp0 = dp1;
13        dp1 = dp2;
14        dp2 = curr;
15    }
16
17    return dp2;
18};
19