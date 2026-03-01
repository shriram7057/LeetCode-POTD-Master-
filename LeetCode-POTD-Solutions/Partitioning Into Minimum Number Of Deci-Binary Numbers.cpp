class Solution {
public:
    int minPartitions(string n) {
        int maxDigit = 0;
        
        for(char c : n) {
            maxDigit = max(maxDigit, c - '0');
            
            // Early stop if we find 9 (maximum possible digit)
            if(maxDigit == 9) return 9;
        }
        
        return maxDigit;
    }
};