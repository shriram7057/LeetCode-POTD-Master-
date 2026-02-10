1var coinChange = function(coins, amount) {
2    const dp = new Array(amount + 1).fill(Infinity);
3    dp[0] = 0;
4
5    for (let coin of coins) {
6        for (let i = coin; i <= amount; i++) {
7            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
8        }
9    }
10
11    return dp[amount] === Infinity ? -1 : dp[amount];
12};
13