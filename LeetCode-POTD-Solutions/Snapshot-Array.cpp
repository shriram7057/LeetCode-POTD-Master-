1class SnapshotArray {
2public:
3    vector<vector<pair<int,int>>> history;
4    int currentSnap;
5
6    SnapshotArray(int length) {
7        history.resize(length);
8        currentSnap = 0;
9        for (int i = 0; i < length; i++) {
10            history[i].push_back({0, 0}); // initial value
11        }
12    }
13    
14    void set(int index, int val) {
15        history[index].push_back({currentSnap, val});
16    }
17    
18    int snap() {
19        return currentSnap++;
20    }
21    
22    int get(int index, int snap_id) {
23        auto &vec = history[index];
24        int left = 0, right = vec.size() - 1;
25        int ans = 0;
26
27        while (left <= right) {
28            int mid = left + (right - left) / 2;
29            if (vec[mid].first <= snap_id) {
30                ans = vec[mid].second;
31                left = mid + 1;
32            } else {
33                right = mid - 1;
34            }
35        }
36        return ans;
37    }
38};
39