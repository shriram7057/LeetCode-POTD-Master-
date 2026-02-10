1class Solution {
2public:
3    char nextGreatestLetter(vector<char>& letters, char target) {
4        int l = 0, r = letters.size() - 1;
5        while (l <= r) {
6            int mid = l + (r - l) / 2;
7            if (letters[mid] <= target) l = mid + 1;
8            else r = mid - 1;
9        }
10        return letters[l % letters.size()];
11    }
12};
13