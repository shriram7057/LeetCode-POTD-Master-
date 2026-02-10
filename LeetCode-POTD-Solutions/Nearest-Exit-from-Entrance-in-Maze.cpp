1class Solution {
2public:
3    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
4        int m = maze.size(), n = maze[0].size();
5        queue<pair<int,int>> q;
6        q.push({entrance[0], entrance[1]});
7        
8        maze[entrance[0]][entrance[1]] = '+'; // mark visited
9        int steps = 0;
10
11        vector<int> dirs = {0, 1, 0, -1, 0};
12
13        while (!q.empty()) {
14            int size = q.size();
15            steps++;
16
17            while (size--) {
18                auto [r, c] = q.front();
19                q.pop();
20
21                for (int i = 0; i < 4; i++) {
22                    int nr = r + dirs[i];
23                    int nc = c + dirs[i + 1];
24
25                    if (nr < 0 || nc < 0 || nr >= m || nc >= n || maze[nr][nc] == '+')
26                        continue;
27
28                    // Check exit condition
29                    if (nr == 0 || nc == 0 || nr == m - 1 || nc == n - 1)
30                        return steps;
31
32                    maze[nr][nc] = '+'; // mark visited
33                    q.push({nr, nc});
34                }
35            }
36        }
37
38        return -1;
39    }
40};
41