1class Solution {
2    public double separateSquares(int[][] squares) {
3        double low = Double.MAX_VALUE, high = Double.MIN_VALUE;
4        for (int[] s : squares) {
5            low = Math.min(low, s[1]);
6            high = Math.max(high, s[1] + s[2]);
7        }
8
9        for (int iter = 0; iter < 100; iter++) {
10            double mid = (low + high) / 2.0;
11            double above = 0, below = 0;
12
13            for (int[] s : squares) {
14                double y = s[1], l = s[2];
15                double top = y + l;
16
17                if (top <= mid) {
18                    below += l * l;
19                } else if (y >= mid) {
20                    above += l * l;
21                } else {
22                    below += (mid - y) * l;
23                    above += (top - mid) * l;
24                }
25            }
26
27            if (below < above) {
28                low = mid;
29            } else {
30                high = mid;
31            }
32        }
33
34        return (low + high) / 2.0;
35    }
36}
37