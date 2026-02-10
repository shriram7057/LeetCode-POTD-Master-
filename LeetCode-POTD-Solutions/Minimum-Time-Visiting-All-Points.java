1class Solution {
2    public int minTimeToVisitAllPoints(int[][] points) {
3        int time = 0;
4        for (int i = 1; i < points.length; i++) {
5            int dx = Math.abs(points[i][0] - points[i - 1][0]);
6            int dy = Math.abs(points[i][1] - points[i - 1][1]);
7            time += Math.max(dx, dy);
8        }
9        return time;
10    }
11}
12