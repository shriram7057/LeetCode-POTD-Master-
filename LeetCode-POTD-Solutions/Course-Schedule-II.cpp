1class Solution {
2public:
3    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
4        vector<vector<int>> graph(numCourses);
5        vector<int> indegree(numCourses, 0);
6
7        // Build graph and indegree
8        for (auto &p : prerequisites) {
9            graph[p[1]].push_back(p[0]);
10            indegree[p[0]]++;
11        }
12
13        queue<int> q;
14        for (int i = 0; i < numCourses; i++) {
15            if (indegree[i] == 0)
16                q.push(i);
17        }
18
19        vector<int> order;
20        while (!q.empty()) {
21            int course = q.front();
22            q.pop();
23            order.push_back(course);
24
25            for (int next : graph[course]) {
26                if (--indegree[next] == 0)
27                    q.push(next);
28            }
29        }
30
31        // If cycle exists
32        if (order.size() != numCourses)
33            return {};
34
35        return order;
36    }
37};
38