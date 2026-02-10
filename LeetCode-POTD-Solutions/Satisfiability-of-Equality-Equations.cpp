1class Solution {
2public:
3    vector<int> parent;
4
5    int find(int x) {
6        if (parent[x] != x)
7            parent[x] = find(parent[x]); // path compression
8        return parent[x];
9    }
10
11    void unite(int x, int y) {
12        int px = find(x);
13        int py = find(y);
14        if (px != py)
15            parent[px] = py;
16    }
17
18    bool equationsPossible(vector<string>& equations) {
19        parent.resize(26);
20        for (int i = 0; i < 26; i++)
21            parent[i] = i;
22
23        // Step 1: handle all equality equations
24        for (auto &eq : equations) {
25            if (eq[1] == '=') {
26                int x = eq[0] - 'a';
27                int y = eq[3] - 'a';
28                unite(x, y);
29            }
30        }
31
32        // Step 2: handle all inequality equations
33        for (auto &eq : equations) {
34            if (eq[1] == '!') {
35                int x = eq[0] - 'a';
36                int y = eq[3] - 'a';
37                if (find(x) == find(y))
38                    return false;
39            }
40        }
41
42        return true;
43    }
44};
45