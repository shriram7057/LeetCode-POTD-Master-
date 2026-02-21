class Solution {
public:
    bool isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    int countPrimeSetBits(int left, int right) {
        int count = 0;
        
        for (int i = left; i <= right; i++) {
            int bits = __builtin_popcount(i);  // count set bits
            if (isPrime(bits)) {
                count++;
            }
        }
        
        return count;
    }
};