class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        long long left = 0, right = 1e18;

        auto can = [&](long long time) {
            long long total = 0;

            for (long long w : workerTimes) {
                long long l = 0, r = mountainHeight;

                while (l <= r) {
                    long long mid = (l + r) / 2;
                    long long need = w * mid * (mid + 1) / 2;

                    if (need <= time) l = mid + 1;
                    else r = mid - 1;
                }

                total += r;
                if (total >= mountainHeight) return true;
            }

            return total >= mountainHeight;
        };

        while (left < right) {
            long long mid = (left + right) / 2;
            if (can(mid)) right = mid;
            else left = mid + 1;
        }

        return left;
    }
};