1class Solution {
2public:
3    vector<vector<int>> result;
4    vector<int> path;
5
6    void dfs(int node, vector<vector<int>>& graph) {
7        path.push_back(node);
8
9        if (node == graph.size() - 1) {
10            result.push_back(path);
11        } else {
12            for (int next : graph[node]) {
13                dfs(next, graph);
14            }
15        }
16
17        path.pop_back(); // backtrack
18    }
19
20    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
21        dfs(0, graph);
22        return result;
23    }
24};
25