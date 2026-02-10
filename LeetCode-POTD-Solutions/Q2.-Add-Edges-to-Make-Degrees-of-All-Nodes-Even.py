class Solution(object):
    def isPossible(self, n, edges):
        g = [set() for _ in range(n)]
        deg = [0] * n

        for a, b in edges:
            a -= 1
            b -= 1
            g[a].add(b)
            g[b].add(a)
            deg[a] += 1
            deg[b] += 1

        odd = [i for i in range(n) if deg[i] % 2 == 1]

        if len(odd) == 0:
            return True
        if len(odd) == 2:
            a, b = odd
            if b not in g[a]:
                return True
            for i in range(n):
                if i != a and i != b and i not in g[a] and i not in g[b]:
                    return True
            return False

        if len(odd) == 4:
            a, b, c, d = odd
            if (b not in g[a] and d not in g[c]) or \
               (c not in g[a] and d not in g[b]) or \
               (d not in g[a] and c not in g[b]):
                return True
            return False

        return False
