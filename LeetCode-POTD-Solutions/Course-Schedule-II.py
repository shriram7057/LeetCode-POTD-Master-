class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        order = []

        while q:
            course = q.popleft()
            order.append(course)
            for nxt in graph[course]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []
