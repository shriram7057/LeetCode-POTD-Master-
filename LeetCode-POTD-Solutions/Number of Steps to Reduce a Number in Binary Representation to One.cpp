class Solution {
public:
    int numSteps(string s) {
        int steps = 0;
        int carry = 0;
        
        // Traverse from right to left (ignore the first bit)
        for (int i = s.size() - 1; i > 0; i--) {
            if ((s[i] - '0' + carry) % 2 == 0) {
                // Even
                steps += 1;
            } else {
                // Odd
                steps += 2;
                carry = 1;
            }
        }
        
        // If there's still a carry at the highest bit
        return steps + carry;
    }
};