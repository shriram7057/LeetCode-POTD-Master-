class Solution:
    def longestCycle(self, V, edges):
        # code here
        
        adj = [-1] * V
        for u ,v in edges:
            adj[u] = v
        visited = [False] * V
        res = -1
        
        for i in range(V):
            if not visited[i]:
                curr = i
                time_map = {}
                step = 0
                
                while curr != -1 and not visited[curr]:
                    visited[curr] = True
                    time_map[curr] = step
                    step += 1
                    curr = adj[curr]
                if curr != -1 and curr in time_map:
                    res = max(res,step - time_map[curr])
        return res