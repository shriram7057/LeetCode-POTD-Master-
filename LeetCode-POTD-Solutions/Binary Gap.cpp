class Solution {
public:
    int binaryGap(int n) {
        int last = -1;      // position of last seen 1
        int maxDist = 0;    // maximum distance
        int position = 0;   // current bit position
        
        while (n > 0) {
            if (n & 1) {  // if current bit is 1
                if (last != -1) {
                    maxDist = max(maxDist, position - last);
                }
                last = position;
            }
            n >>= 1;      // shift right
            position++;
        }
        
        return maxDist;
    }
};