1class Solution(object):
2    def findAllPeople(self, n, meetings, firstPerson):
3        from collections import defaultdict, deque
4        
5        meetings.sort(key=lambda x: x[2])
6        has_secret = set([0, firstPerson])
7        i = 0
8        
9        while i < len(meetings):
10            t = meetings[i][2]
11            graph = defaultdict(list)
12            people = set()
13            
14            while i < len(meetings) and meetings[i][2] == t:
15                x, y, _ = meetings[i]
16                graph[x].append(y)
17                graph[y].append(x)
18                people.add(x)
19                people.add(y)
20                i += 1
21            
22            q = deque(p for p in people if p in has_secret)
23            visited = set(q)
24            
25            while q:
26                u = q.popleft()
27                for v in graph[u]:
28                    if v not in visited:
29                        visited.add(v)
30                        q.append(v)
31            
32            has_secret |= visited
33        
34        return list(has_secret)
35