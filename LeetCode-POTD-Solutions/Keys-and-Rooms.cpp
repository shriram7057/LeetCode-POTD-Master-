1class Solution {
2public:
3    void dfs(int room, vector<vector<int>>& rooms, vector<bool>& visited) {
4        visited[room] = true;
5
6        for (int key : rooms[room]) {
7            if (!visited[key]) {
8                dfs(key, rooms, visited);
9            }
10        }
11    }
12
13    bool canVisitAllRooms(vector<vector<int>>& rooms) {
14        int n = rooms.size();
15        vector<bool> visited(n, false);
16
17        dfs(0, rooms, visited);
18
19        for (bool v : visited) {
20            if (!v) return false;
21        }
22        return true;
23    }
24};
25