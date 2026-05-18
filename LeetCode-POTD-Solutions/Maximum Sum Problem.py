class Solution {
  public:
    
    unordered_map<int, int> dp;
    
    int maxSum(int n) {
        if(n == 0)
            return 0;
        
        if(dp.count(n))
            return dp[n];
        
        return dp[n] = max(n,
                           maxSum(n / 2) +
                           maxSum(n / 3) +
                           maxSum(n / 4));
    }
};