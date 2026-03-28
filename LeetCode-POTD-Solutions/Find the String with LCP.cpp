class Solution {
public:
    string findTheString(vector<vector<int>>& lcp) {
        int n = lcp.size();
        
        // Step 1: Validate diagonal
        for (int i = 0; i < n; i++) {
            if (lcp[i][i] != n - i) return "";
        }
        
        // Step 2: Build string greedily
        string res(n, '#');
        char cur = 'a';
        
        for (int i = 0; i < n; i++) {
            if (res[i] == '#') {
                if (cur > 'z') return "";
                for (int j = i; j < n; j++) {
                    if (lcp[i][j] > 0) {
                        res[j] = cur;
                    }
                }
                cur++;
            }
        }
        
        // Step 3: Verify using LCP recomputation
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (res[i] == res[j]) {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                }
            }
        }
        
        // Step 4: Compare with given lcp
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] != lcp[i][j]) return "";
            }
        }
        
        return res;
    }
};