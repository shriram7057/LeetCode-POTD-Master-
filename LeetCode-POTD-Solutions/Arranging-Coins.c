1int arrangeCoins(int n) {
2    long long left = 0, right = n;
3    int ans = 0;
4
5    while (left <= right) {
6        long long mid = left + (right - left) / 2;
7        long long coins = mid * (mid + 1) / 2;
8
9        if (coins <= n) {
10            ans = mid;          // mid rows can be completed
11            left = mid + 1;
12        } else {
13            right = mid - 1;
14        }
15    }
16    return ans;
17}
18