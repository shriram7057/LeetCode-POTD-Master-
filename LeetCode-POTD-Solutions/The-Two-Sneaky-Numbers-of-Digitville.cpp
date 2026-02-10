class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_map<int, int> count;
        vector<int> ans;
        for (int num : nums) {
            count[num]++;
        }
        for (auto &p : count) {
            if (p.second == 2)
                ans.push_back(p.first);
        }
        return ans;
    }
};
