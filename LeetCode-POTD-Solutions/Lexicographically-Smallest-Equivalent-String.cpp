1class Solution {
2public:
3    vector<int> parent;
4
5    int find(int x) {
6        if (parent[x] != x)
7            parent[x] = find(parent[x]);
8        return parent[x];
9    }
10
11    void unite(int x, int y) {
12        int px = find(x);
13        int py = find(y);
14        if (px == py) return;
15
16        // Attach larger to smaller to keep lexicographically smallest root
17        if (px < py)
18            parent[py] = px;
19        else
20            parent[px] = py;
21    }
22
23    string smallestEquivalentString(string s1, string s2, string baseStr) {
24        parent.resize(26);
25        for (int i = 0; i < 26; i++)
26            parent[i] = i;
27
28        // Step 1: Build equivalence classes
29        for (int i = 0; i < s1.size(); i++) {
30            unite(s1[i] - 'a', s2[i] - 'a');
31        }
32
33        // Step 2: Transform baseStr
34        for (char &c : baseStr) {
35            c = find(c - 'a') + 'a';
36        }
37
38        return baseStr;
39    }
40};
41