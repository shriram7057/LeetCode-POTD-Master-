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
14        if (px != py)
15            parent[px] = py;
16    }
17
18    bool isSimilar(const string &a, const string &b) {
19        int diff = 0;
20        for (int i = 0; i < a.size(); i++) {
21            if (a[i] != b[i]) {
22                diff++;
23                if (diff > 2) return false;
24            }
25        }
26        return diff == 0 || diff == 2;
27    }
28
29    int numSimilarGroups(vector<string>& strs) {
30        int n = strs.size();
31        parent.resize(n);
32        for (int i = 0; i < n; i++)
33            parent[i] = i;
34
35        for (int i = 0; i < n; i++) {
36            for (int j = i + 1; j < n; j++) {
37                if (isSimilar(strs[i], strs[j])) {
38                    unite(i, j);
39                }
40            }
41        }
42
43        int groups = 0;
44        for (int i = 0; i < n; i++) {
45            if (find(i) == i)
46                groups++;
47        }
48        return groups;
49    }
50};
51