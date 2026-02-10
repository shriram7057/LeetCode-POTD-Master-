1class Solution {
2    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
3        int n = numberOfUsers;
4        int[] mentions = new int[n];
5        boolean[] online = new boolean[n];
6        Arrays.fill(online, true);
7
8        // Convert events into a sortable structure
9        class E {
10            String type, arg;
11            int time;
12            E(String a, int b, String c){ type=a; time=b; arg=c; }
13        }
14
15        List<E> list = new ArrayList<>();
16        for (var e : events) {
17            list.add(new E(e.get(0), Integer.parseInt(e.get(1)), e.get(2)));
18        }
19
20        // Sort by timestamp, and OFFLINE before MESSAGE at same timestamp
21        Collections.sort(list, (a,b) -> {
22            if (a.time != b.time) return a.time - b.time;
23            if (!a.type.equals(b.type))
24                return a.type.equals("OFFLINE") ? -1 : 1;
25            return 0;
26        });
27
28        // Min-heap for restoration
29        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x[0]));
30
31        for (E e : list) {
32            int t = e.time;
33
34            // Restore users first
35            while (!pq.isEmpty() && pq.peek()[0] <= t) {
36                int[] top = pq.poll();
37                online[top[1]] = true;
38            }
39
40            if (e.type.equals("OFFLINE")) {
41                int u = Integer.parseInt(e.arg);
42                if (online[u]) {
43                    online[u] = false;
44                    pq.add(new int[]{t + 60, u});
45                }
46            } 
47            else { // MESSAGE
48                String[] tokens = e.arg.split(" ");
49                for (String tok : tokens) {
50                    if (tok.equals("ALL")) {
51                        for (int i = 0; i < n; i++) mentions[i]++;
52                    } 
53                    else if (tok.equals("HERE")) {
54                        for (int i = 0; i < n; i++)
55                            if (online[i]) mentions[i]++;
56                    } 
57                    else if (tok.startsWith("id")) {
58                        int u = Integer.parseInt(tok.substring(2));
59                        mentions[u]++;
60                    }
61                }
62            }
63        }
64
65        return mentions;
66    }
67}
68