1class Solution {
2public:
3    int findLongestChain(vector<vector<int>>& pairs) {
4        // Sort by second element (ending value)
5        sort(pairs.begin(), pairs.end(),
6             [](const vector<int>& a, const vector<int>& b) {
7                 return a[1] < b[1];
8             });
9
10        int count = 0;
11        int currEnd = INT_MIN;
12
13        for (auto& p : pairs) {
14            if (p[0] > currEnd) {
15                count++;
16                currEnd = p[1];
17            }
18        }
19
20        return count;
21    }
22};
23