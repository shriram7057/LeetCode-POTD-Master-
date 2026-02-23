class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int n = s.size();
        if (n < k) return false;

        int total = 1 << k;  // 2^k
        vector<bool> seen(total, false);
        
        int mask = 0;
        int allOnes = total - 1;
        int count = 0;

        for (int i = 0; i < n; i++) {
            // Shift left and add current bit
            mask = ((mask << 1) & allOnes) | (s[i] - '0');

            // Start checking only when we have k bits
            if (i >= k - 1) {
                if (!seen[mask]) {
                    seen[mask] = true;
                    count++;
                    if (count == total) return true;
                }
            }
        }
        return false;
    }
};