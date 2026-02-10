1class Solution {
2public:
3    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
4        sort(potions.begin(), potions.end());
5        int m = potions.size();
6        vector<int> res;
7
8        for (int s : spells) {
9            long long need = (success + s - 1) / s; // ceiling division
10            int idx = lower_bound(potions.begin(), potions.end(), need) - potions.begin();
11            res.push_back(m - idx);
12        }
13
14        return res;
15    }
16};
17