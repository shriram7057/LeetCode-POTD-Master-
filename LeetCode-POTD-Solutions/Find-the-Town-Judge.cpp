1class Solution {
2public:
3    int findJudge(int n, vector<vector<int>>& trust) {
4        vector<int> in(n + 1, 0), out(n + 1, 0);
5
6        for (auto& t : trust) {
7            out[t[0]]++;   // t[0] trusts someone
8            in[t[1]]++;    // t[1] is trusted
9        }
10
11        for (int i = 1; i <= n; i++) {
12            if (in[i] == n - 1 && out[i] == 0)
13                return i;
14        }
15
16        return -1;
17    }
18};
19