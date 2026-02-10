1class Solution {
2    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
3        int n = bottomLeft.length;
4        long ans = 0;
5
6        for (int i = 0; i < n; i++) {
7            for (int j = i + 1; j < n; j++) {
8                int x1 = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
9                int y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
10                int x2 = Math.min(topRight[i][0], topRight[j][0]);
11                int y2 = Math.min(topRight[i][1], topRight[j][1]);
12
13                if (x1 < x2 && y1 < y2) {
14                    long side = Math.min(x2 - x1, y2 - y1);
15                    ans = Math.max(ans, side * side);
16                }
17            }
18        }
19        return ans;
20    }
21}
22