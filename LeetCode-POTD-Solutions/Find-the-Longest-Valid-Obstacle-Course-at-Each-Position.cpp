1class Solution {
2public:
3    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
4        vector<int> tails;     // tails[i] = smallest possible tail of LNDS length i+1
5        vector<int> answer;
6
7        for (int x : obstacles) {
8            // upper_bound allows non-decreasing sequence
9            auto it = upper_bound(tails.begin(), tails.end(), x);
10
11            if (it == tails.end()) {
12                tails.push_back(x);
13                answer.push_back(tails.size());
14            } else {
15                *it = x;
16                answer.push_back(it - tails.begin() + 1);
17            }
18        }
19
20        return answer;
21    }
22};
23