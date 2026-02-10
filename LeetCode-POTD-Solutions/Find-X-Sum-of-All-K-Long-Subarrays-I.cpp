class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        vector<int> ans;
        
        for (int i = 0; i + k <= n; ++i) {
            unordered_map<int, int> freq;
            
            // Count frequency in current window
            for (int j = i; j < i + k; ++j)
                freq[nums[j]]++;
            
            // Create a list of (frequency, value)
            vector<pair<int, int>> freqList;
            for (auto& p : freq)
                freqList.push_back({p.second, p.first});
            
            // Sort by frequency desc, then value desc
            sort(freqList.begin(), freqList.end(), [&](auto& a, auto& b) {
                if (a.first == b.first) return a.second > b.second;
                return a.first > b.first;
            });
            
            int sum = 0;
            // Take top x elements
            for (int t = 0; t < x && t < freqList.size(); ++t)
                sum += freqList[t].first * freqList[t].second;
            
            ans.push_back(sum);
        }
        
        return ans;
    }
};
