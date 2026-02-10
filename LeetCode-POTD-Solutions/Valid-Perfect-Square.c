1#include <stdbool.h>
2
3bool isPerfectSquare(int num) {
4    long long left = 1, right = num;
5
6    while (left <= right) {
7        long long mid = left + (right - left) / 2;
8        long long square = mid * mid;
9
10        if (square == num) {
11            return true;
12        } else if (square < num) {
13            left = mid + 1;
14        } else {
15            right = mid - 1;
16        }
17    }
18    return false;
19}
20