1import java.util.*;
2
3class Solution {
4    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
5        int maxH = longestConsecutive(hBars);
6        int maxV = longestConsecutive(vBars);
7        int side = Math.min(maxH, maxV);
8        return side * side;
9    }
10
11    private int longestConsecutive(int[] bars) {
12        if (bars.length == 0) return 1;
13        Arrays.sort(bars);
14        int max = 1, cur = 1;
15        for (int i = 1; i < bars.length; i++) {
16            if (bars[i] == bars[i - 1] + 1) {
17                cur++;
18            } else {
19                cur = 1;
20            }
21            max = Math.max(max, cur);
22        }
23        return max + 1;
24    }
25}
26