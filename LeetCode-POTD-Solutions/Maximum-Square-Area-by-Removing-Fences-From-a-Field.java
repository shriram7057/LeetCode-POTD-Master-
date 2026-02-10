1import java.util.*;
2
3class Solution {
4    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
5        final long MOD = 1000000007L;
6
7        List<Integer> hs = new ArrayList<>();
8        List<Integer> vs = new ArrayList<>();
9
10        hs.add(1);
11        hs.add(m);
12        for (int x : hFences) hs.add(x);
13
14        vs.add(1);
15        vs.add(n);
16        for (int x : vFences) vs.add(x);
17
18        Collections.sort(hs);
19        Collections.sort(vs);
20
21        Set<Integer> hDiff = new HashSet<>();
22        for (int i = 0; i < hs.size(); i++) {
23            for (int j = i + 1; j < hs.size(); j++) {
24                hDiff.add(hs.get(j) - hs.get(i));
25            }
26        }
27
28        long maxSide = -1;
29        for (int i = 0; i < vs.size(); i++) {
30            for (int j = i + 1; j < vs.size(); j++) {
31                int d = vs.get(j) - vs.get(i);
32                if (hDiff.contains(d)) {
33                    maxSide = Math.max(maxSide, d);
34                }
35            }
36        }
37
38        if (maxSide == -1) return -1;
39        return (int)((maxSide * maxSide) % MOD);
40    }
41}
42