1class Solution {
2public:
3    bool isTrionic(vector<int>& nums) {
4        int n = nums.size();
5        if (n < 3) return false;
6
7        int i = 0;
8
9        // strictly increasing
10        while (i + 1 < n && nums[i] < nums[i + 1]) i++;
11        if (i == 0 || i == n - 1) return false;
12
13        // strictly decreasing
14        int p = i;
15        while (i + 1 < n && nums[i] > nums[i + 1]) i++;
16        if (i == p || i == n - 1) return false;
17
18        // strictly increasing
19        while (i + 1 < n && nums[i] < nums[i + 1]) i++;
20
21        return i == n - 1;
22    }
23};
24