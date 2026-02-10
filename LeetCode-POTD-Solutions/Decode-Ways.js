1var numDecodings = function(s) {
2    if (s[0] === '0') return 0;
3
4    let prev2 = 1; // dp[i-2]
5    let prev1 = 1; // dp[i-1]
6
7    for (let i = 1; i < s.length; i++) {
8        let curr = 0;
9
10        // Single digit decode
11        if (s[i] !== '0') {
12            curr += prev1;
13        }
14
15        // Two digit decode
16        const twoDigit = parseInt(s.substring(i - 1, i + 1));
17        if (twoDigit >= 10 && twoDigit <= 26) {
18            curr += prev2;
19        }
20
21        prev2 = prev1;
22        prev1 = curr;
23
24        if (curr === 0) return 0; // early stop if invalid
25    }
26
27    return prev1;
28};
29