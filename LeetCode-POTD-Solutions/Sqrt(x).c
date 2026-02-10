1int mySqrt(int x) {
2    if (x < 2) return x;
3
4    long long left = 1, right = x / 2;
5    int ans = 0;
6
7    while (left <= right) {
8        long long mid = left + (right - left) / 2;
9        long long square = mid * mid;
10
11        if (square == x) {
12            return (int)mid;
13        } else if (square < x) {
14            ans = mid;        // mid is a valid candidate
15            left = mid + 1;
16        } else {
17            right = mid - 1;
18        }
19    }
20    return ans;
21}
22