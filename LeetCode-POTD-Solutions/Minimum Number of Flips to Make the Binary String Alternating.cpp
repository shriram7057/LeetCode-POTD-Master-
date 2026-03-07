class Solution {
public:
    int minFlips(string s) {
        int n = s.size();
        string t = s + s;

        int diff1 = 0, diff2 = 0;
        int ans = INT_MAX;

        for (int i = 0; i < 2 * n; i++) {
            char expected1 = (i % 2) ? '1' : '0'; // 0101...
            char expected2 = (i % 2) ? '0' : '1'; // 1010...

            if (t[i] != expected1) diff1++;
            if (t[i] != expected2) diff2++;

            if (i >= n) {
                char prev_expected1 = ((i - n) % 2) ? '1' : '0';
                char prev_expected2 = ((i - n) % 2) ? '0' : '1';

                if (t[i - n] != prev_expected1) diff1--;
                if (t[i - n] != prev_expected2) diff2--;
            }

            if (i >= n - 1) {
                ans = min(ans, min(diff1, diff2));
            }
        }

        return ans;
    }
};