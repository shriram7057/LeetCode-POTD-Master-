class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        
        // We only need up to 100 rows
        vector<vector<double>> dp(101, vector<double>(101, 0.0));
        
        dp[0][0] = poured;
        
        for (int i = 0; i <= query_row; i++) {
            for (int j = 0; j <= i; j++) {
                
                if (dp[i][j] > 1.0) {
                    double overflow = (dp[i][j] - 1.0) / 2.0;
                    
                    dp[i+1][j]     += overflow;
                    dp[i+1][j+1]   += overflow;
                    
                    dp[i][j] = 1.0; // cap current glass
                }
            }
        }
        
        return dp[query_row][query_glass];
    }
};