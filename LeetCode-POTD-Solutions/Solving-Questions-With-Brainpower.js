1var mostPoints = function(questions) {
2    const n = questions.length;
3    const dp = new Array(n + 1).fill(0);
4
5    // Process from right to left
6    for (let i = n - 1; i >= 0; i--) {
7        const points = questions[i][0];
8        const brainpower = questions[i][1];
9
10        const nextIndex = i + brainpower + 1;
11        const take = points + (nextIndex < n ? dp[nextIndex] : 0);
12        const skip = dp[i + 1];
13
14        dp[i] = Math.max(take, skip);
15    }
16
17    return dp[0];
18};
19