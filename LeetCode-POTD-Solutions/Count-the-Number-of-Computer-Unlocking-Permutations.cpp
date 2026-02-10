1class Solution {
2public:
3    static const int MOD = 1'000'000'007;
4
5    long long modpow(long long a, long long e) {
6        long long r = 1;
7        while (e) {
8            if (e & 1) r = r * a % MOD;
9            a = a * a % MOD;
10            e >>= 1;
11        }
12        return r;
13    }
14
15    long long modinv(long long a) { return modpow(a, MOD - 2); }
16
17    int countPermutations(vector<int>& complexity) {
18        int n = complexity.size();
19        vector<int> idx(n);
20        iota(idx.begin(), idx.end(), 0);
21
22        // Group by complexity (sort indices by complexity then id)
23        sort(idx.begin(), idx.end(), [&](int a, int b){
24            if (complexity[a] != complexity[b]) return complexity[a] < complexity[b];
25            return a < b;
26        });
27
28        // Precompute factorials
29        vector<long long> fact(n+1), invfact(n+1);
30        fact[0] = 1;
31        for (int i = 1; i <= n; i++) fact[i] = fact[i-1] * i % MOD;
32        invfact[n] = modinv(fact[n]);
33        for (int i = n-1; i >= 0; i--) invfact[i] = invfact[i+1] * (i+1) % MOD;
34
35        long long answer = 1;
36        int used = 1;  // computer 0 is already unlocked
37
38        int i = 1;
39        while (i < n) {
40            int j = i;
41            int cx = complexity[idx[i]];
42            while (j < n && complexity[idx[j]] == cx) j++;
43
44            int m = j - i;  // size of this group
45
46            // Check unlockability: each i in group needs a predecessor
47            for (int k = i; k < j; k++) {
48                int node = idx[k];
49                bool ok = false;
50                for (int p = 0; p < node; p++) {
51                    if (complexity[p] < cx) {
52                        ok = true;
53                        break;
54                    }
55                }
56                if (!ok) return 0;
57            }
58
59            // Place these m nodes among the "used + m - 1" positions
60            long long ways = fact[used + m - 1] * invfact[used - 1] % MOD;
61            ways = ways * invfact[m] % MOD;
62            ways = ways * fact[m] % MOD;
63
64            answer = answer * ways % MOD;
65            used += m;
66            i = j;
67        }
68        return answer % MOD;
69    }
70};
71