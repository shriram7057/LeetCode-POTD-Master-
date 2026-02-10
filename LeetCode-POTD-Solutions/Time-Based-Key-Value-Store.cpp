1class TimeMap {
2public:
3    unordered_map<string, vector<pair<int, string>>> mp;
4
5    TimeMap() {
6    }
7    
8    void set(string key, string value, int timestamp) {
9        mp[key].push_back({timestamp, value});
10    }
11    
12    string get(string key, int timestamp) {
13        if (mp.find(key) == mp.end()) return "";
14
15        auto &values = mp[key];
16        int left = 0, right = values.size() - 1;
17        string result = "";
18
19        while (left <= right) {
20            int mid = left + (right - left) / 2;
21            if (values[mid].first <= timestamp) {
22                result = values[mid].second; // valid candidate
23                left = mid + 1;              // try to find a later timestamp
24            } else {
25                right = mid - 1;
26            }
27        }
28        return result;
29    }
30};
31