1class Solution {
2public:
3    vector<int> findRightInterval(vector<vector<int>>& intervals) {
4        int n = intervals.size();
5
6        // store (start, original index)
7        vector<pair<int,int>> starts;
8        for (int i = 0; i < n; i++) {
9            starts.push_back({intervals[i][0], i});
10        }
11
12        // sort by start
13        sort(starts.begin(), starts.end());
14
15        vector<int> result(n, -1);
16
17        // for each interval, binary search on starts
18        for (int i = 0; i < n; i++) {
19            int end = intervals[i][1];
20            int left = 0, right = n - 1;
21            int pos = -1;
22
23            while (left <= right) {
24                int mid = left + (right - left) / 2;
25                if (starts[mid].first >= end) {
26                    pos = mid;
27                    right = mid - 1;  // try to find smaller valid start
28                } else {
29                    left = mid + 1;
30                }
31            }
32
33            if (pos != -1) {
34                result[i] = starts[pos].second;
35            }
36        }
37
38        return result;
39    }
40};
41