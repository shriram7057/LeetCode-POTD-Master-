class Solution {
public:
    int reverseBits(int n) {
        unsigned int result = 0;
        
        for (int i = 0; i < 32; i++) {
            result <<= 1;        // Make space
            result |= (n & 1);   // Add last bit of n
            n >>= 1;             // Shift n to process next bit
        }
        
        return result;
    }
};