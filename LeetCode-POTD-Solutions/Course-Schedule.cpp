1class Solution {
2public:
3    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
4        vector<vector<int>> graph(numCourses);
5        vector<int> indegree(numCourses, 0);
6
7        for (auto &p : prerequisites) {
8            graph[p[1]].push_back(p[0]);
9            indegree[p[0]]++;
10        }
11
12        queue<int> q;
13        for (int i = 0; i < numCourses; i++) {
14            if (indegree[i] == 0)
15                q.push(i);
16        }
17
18        int taken = 0;
19        while (!q.empty()) {
20            int course = q.front();
21            q.pop();
22            taken++;
23
24            for (int next : graph[course]) {
25                if (--indegree[next] == 0)
26                    q.push(next);
27            }
28        }
29
30        return taken == numCourses;
31    }
32};
33