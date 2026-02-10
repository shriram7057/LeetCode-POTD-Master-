class Solution(object):
    def minReorder(self, n, connections):
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        # Build graph: store directed edges and undirected edges
        for a, b in connections:
            graph[a].append((b, 1))  # edge originally a -> b
            graph[b].append((a, 0))  # reverse edge b -> a (no need to reorder)
        
        q = deque([0])
        visited = set([0])
        changes = 0
        
        while q:
            node = q.popleft()
            for nei, cost in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    changes += cost
                    q.append(nei)
        
        return changes
