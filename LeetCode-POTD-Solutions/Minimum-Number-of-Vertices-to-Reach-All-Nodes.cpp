1class Solution {
2public:
3    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
4        vector<int> indegree(n, 0);
5
6        for (auto& e : edges) {
7            indegree[e[1]]++;
8        }
9
10        vector<int> result;
11        for (int i = 0; i < n; i++) {
12            if (indegree[i] == 0) {
13                result.push_back(i);
14            }
15        }
16
17        return result;
18    }
19};
20