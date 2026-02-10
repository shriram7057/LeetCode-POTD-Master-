1class Solution {
2
3    public int countTrapezoids(int[][] points) {
4        int n = points.length;
5        double inf = 1e9 + 7;
6        Map<Double, List<Double>> slopeToIntercept = new HashMap<>();
7        Map<Integer, List<Double>> midToSlope = new HashMap<>();
8        int ans = 0;
9
10        for (int i = 0; i < n; i++) {
11            int x1 = points[i][0];
12            int y1 = points[i][1];
13            for (int j = i + 1; j < n; j++) {
14                int x2 = points[j][0];
15                int y2 = points[j][1];
16                int dx = x1 - x2;
17                int dy = y1 - y2;
18                double k;
19                double b;
20
21                if (x2 == x1) {
22                    k = inf;
23                    b = x1;
24                } else {
25                    k = (1.0 * (y2 - y1)) / (x2 - x1);
26                    b = (1.0 * (y1 * dx - x1 * dy)) / dx;
27                }
28                if (k == -0.0) {
29                    k = 0.0;
30                }
31                if (b == -0.0) {
32                    b = 0.0;
33                }
34                int mid = (x1 + x2) * 10000 + (y1 + y2);
35                slopeToIntercept
36                    .computeIfAbsent(k, key -> new ArrayList<>())
37                    .add(b);
38                midToSlope
39                    .computeIfAbsent(mid, key -> new ArrayList<>())
40                    .add(k);
41            }
42        }
43
44        for (List<Double> sti : slopeToIntercept.values()) {
45            if (sti.size() == 1) {
46                continue;
47            }
48            Map<Double, Integer> cnt = new TreeMap<>();
49            for (double b : sti) {
50                cnt.put(b, cnt.getOrDefault(b, 0) + 1);
51            }
52            int sum = 0;
53            for (int count : cnt.values()) {
54                ans += sum * count;
55                sum += count;
56            }
57        }
58
59        for (List<Double> mts : midToSlope.values()) {
60            if (mts.size() == 1) {
61                continue;
62            }
63            Map<Double, Integer> cnt = new TreeMap<>();
64            for (double k : mts) {
65                cnt.put(k, cnt.getOrDefault(k, 0) + 1);
66            }
67            int sum = 0;
68            for (int count : cnt.values()) {
69                ans -= sum * count;
70                sum += count;
71            }
72        }
73
74        return ans;
75    }
76}