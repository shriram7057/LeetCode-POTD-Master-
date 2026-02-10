1class Solution {
2public:
3    int minMutation(string startGene, string endGene, vector<string>& bank) {
4        unordered_set<string> dict(bank.begin(), bank.end());
5        if (!dict.count(endGene)) return -1;
6
7        queue<string> q;
8        unordered_set<string> visited;
9        q.push(startGene);
10        visited.insert(startGene);
11
12        string genes = "ACGT";
13        int steps = 0;
14
15        while (!q.empty()) {
16            int size = q.size();
17            while (size--) {
18                string curr = q.front();
19                q.pop();
20
21                if (curr == endGene) return steps;
22
23                for (int i = 0; i < 8; i++) {
24                    char original = curr[i];
25                    for (char g : genes) {
26                        if (g == original) continue;
27                        curr[i] = g;
28
29                        if (dict.count(curr) && !visited.count(curr)) {
30                            visited.insert(curr);
31                            q.push(curr);
32                        }
33                    }
34                    curr[i] = original; // restore
35                }
36            }
37            steps++;
38        }
39        return -1;
40    }
41};
42