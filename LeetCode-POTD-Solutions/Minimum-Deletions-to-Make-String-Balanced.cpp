1class Solution {
2public:
3    int minimumDeletions(string s) {
4        int countB = 0;     // number of 'b's seen so far
5        int deletions = 0;  // minimum deletions needed
6
7        for (char c : s) {
8            if (c == 'b') {
9                countB++;
10            } else { // c == 'a'
11                deletions = min(deletions + 1, countB);
12            }
13        }
14
15        return deletions;
16    }
17};