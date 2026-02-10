1class Solution(object):
2    def separateSquares(self, squares):
3        import bisect
4        events = []
5        for x, y, l in squares:
6            events.append((y, x, x + l, 1))
7            events.append((y + l, x, x + l, -1))
8
9        events.sort()
10        xs = []
11        active = []
12        area_segments = []
13        total_area = 0.0
14
15        def union_length(intervals):
16            if not intervals:
17                return 0
18            intervals.sort()
19            length = 0
20            s, e = intervals[0]
21            for ns, ne in intervals[1:]:
22                if ns > e:
23                    length += e - s
24                    s, e = ns, ne
25                else:
26                    e = max(e, ne)
27            return length + (e - s)
28
29        prev_y = events[0][0]
30        i = 0
31
32        while i < len(events):
33            y = events[i][0]
34            dy = y - prev_y
35            if dy > 0:
36                width = union_length(active)
37                area = width * dy
38                area_segments.append((prev_y, y, width, total_area))
39                total_area += area
40                prev_y = y
41
42            while i < len(events) and events[i][0] == y:
43                _, x1, x2, t = events[i]
44                if t == 1:
45                    active.append((x1, x2))
46                else:
47                    active.remove((x1, x2))
48                i += 1
49
50        half = total_area / 2.0
51
52        for y1, y2, w, acc in area_segments:
53            area = w * (y2 - y1)
54            if acc + area >= half:
55                return y1 + (half - acc) / w
56
57        return events[-1][0]
58