1class Solution {
2public:
3    vector<long long> prefix;
4    long long total;
5
6    Solution(vector<int>& w) {
7        total = 0;
8        for (int x : w) {
9            total += x;
10            prefix.push_back(total);
11        }
12    }
13    
14    int pickIndex() {
15        long long r = rand() % total + 1;
16        return lower_bound(prefix.begin(), prefix.end(), r) - prefix.begin();
17    }
18};
19