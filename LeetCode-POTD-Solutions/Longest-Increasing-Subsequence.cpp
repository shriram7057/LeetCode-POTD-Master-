1class Solution {
2public:
3    int lengthOfLIS(vector<int>& nums) {
4        vector<int> tails;
5
6        for (int num : nums) {
7            int l = 0, r = tails.size();
8            while (l < r) {
9                int mid = l + (r - l) / 2;
10                if (tails[mid] < num)
11                    l = mid + 1;
12                else
13                    r = mid;
14            }
15            if (l == tails.size())
16                tails.push_back(num);
17            else
18                tails[l] = num;
19        }
20
21        return tails.size();
22    }
23};
24