1class Solution {
2public:
3    int shortestPathAllKeys(vector<string>& grid) {
4        int m = grid.size();
5        int n = grid[0].size();
6
7        int startR, startC;
8        int keyCount = 0;
9
10        // Find start and count keys
11        for (int i = 0; i < m; i++) {
12            for (int j = 0; j < n; j++) {
13                if (grid[i][j] == '@') {
14                    startR = i;
15                    startC = j;
16                } else if (grid[i][j] >= 'a' && grid[i][j] <= 'f') {
17                    keyCount++;
18                }
19            }
20        }
21
22        int allKeysMask = (1 << keyCount) - 1;
23
24        queue<tuple<int, int, int>> q;
25        vector<vector<vector<bool>>> visited(
26            m, vector<vector<bool>>(n, vector<bool>(1 << keyCount, false))
27        );
28
29        q.push({startR, startC, 0});
30        visited[startR][startC][0] = true;
31
32        vector<int> dirs = {0, 1, 0, -1, 0};
33        int steps = 0;
34
35        while (!q.empty()) {
36            int size = q.size();
37
38            while (size--) {
39                auto [r, c, mask] = q.front();
40                q.pop();
41
42                if (mask == allKeysMask)
43                    return steps;
44
45                for (int d = 0; d < 4; d++) {
46                    int nr = r + dirs[d];
47                    int nc = c + dirs[d + 1];
48                    int newMask = mask;
49
50                    if (nr < 0 || nr >= m || nc < 0 || nc >= n)
51                        continue;
52
53                    char cell = grid[nr][nc];
54                    if (cell == '#') continue;
55
56                    // Lock
57                    if (cell >= 'A' && cell <= 'F') {
58                        int keyBit = cell - 'A';
59                        if (!(mask & (1 << keyBit)))
60                            continue;
61                    }
62
63                    // Key
64                    if (cell >= 'a' && cell <= 'f') {
65                        int keyBit = cell - 'a';
66                        newMask |= (1 << keyBit);
67                    }
68
69                    if (!visited[nr][nc][newMask]) {
70                        visited[nr][nc][newMask] = true;
71                        q.push({nr, nc, newMask});
72                    }
73                }
74            }
75            steps++;
76        }
77
78        return -1;
79    }
80};
81