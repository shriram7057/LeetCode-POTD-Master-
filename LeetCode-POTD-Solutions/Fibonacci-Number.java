1class Solution {
2    public int fib(int n) {
3        if (n < 2) return n;
4
5        int a = 0, b = 1;
6        for (int i = 2; i <= n; i++) {
7            int c = a + b;
8            a = b;
9            b = c;
10        }
11        return b;
12    }
13}
14