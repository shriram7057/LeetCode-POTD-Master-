class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        indegree = [0] * n
        
        for a, b in edges:
            indegree[b] += 1
        
        return [i for i in range(n) if indegree[i] == 0]
