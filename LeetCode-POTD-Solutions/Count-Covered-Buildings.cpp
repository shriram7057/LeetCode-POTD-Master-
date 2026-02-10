1class Solution {
2public:
3    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
4        // Group by row (x) and column (y)
5        unordered_map<int, vector<int>> row, col;
6
7        for (auto &b : buildings) {
8            int x = b[0];
9            int y = b[1];
10            row[x].push_back(y);
11            col[y].push_back(x);
12        }
13
14        // Sort each row and column list
15        for (auto &p : row) sort(p.second.begin(), p.second.end());
16        for (auto &p : col) sort(p.second.begin(), p.second.end());
17
18        int covered = 0;
19
20        for (auto &b : buildings) {
21            int x = b[0];
22            int y = b[1];
23
24            auto &rowList = row[x];
25            auto &colList = col[y];
26
27            // Row check
28            bool left = false, right = false;
29
30            auto it = lower_bound(rowList.begin(), rowList.end(), y);
31            int pos = it - rowList.begin();
32
33            if (pos > 0) left = true;
34            if (pos < rowList.size() - 1) right = true;
35
36            if (!left || !right) continue;
37
38            // Column check
39            bool up = false, down = false;
40
41            auto it2 = lower_bound(colList.begin(), colList.end(), x);
42            int pos2 = it2 - colList.begin();
43
44            if (pos2 > 0) up = true;
45            if (pos2 < colList.size() - 1) down = true;
46
47            if (up && down) covered++;
48        }
49
50        return covered;
51    }
52};
53