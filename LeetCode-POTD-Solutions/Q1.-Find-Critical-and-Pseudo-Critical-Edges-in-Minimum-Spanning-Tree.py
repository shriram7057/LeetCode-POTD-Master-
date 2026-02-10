class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Add original index
        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda x: x[2])

        # DSU
        def find(p, x):
            if p[x] != x:
                p[x] = find(p, p[x])
            return p[x]

        def union(p, r, a, b):
            pa = find(p, a)
            pb = find(p, b)
            if pa == pb:
                return False
            if r[pa] < r[pb]:
                pa, pb = pb, pa
            p[pb] = pa
            if r[pa] == r[pb]:
                r[pa] += 1
            return True

        # MST weight with optional forced edge and optional blocked edge
        def kruskal(blocked, forced):
            p = list(range(n))
            r = [0] * n
            weight = 0
            cnt = 0

            if forced != -1:
                a, b, w, _ = edges[forced]
                if union(p, r, a, b):
                    weight += w
                    cnt += 1

            for i, (a, b, w, _) in enumerate(edges):
                if i == blocked:
                    continue
                if union(p, r, a, b):
                    weight += w
                    cnt += 1
                if cnt == n - 1:
                    break

            return weight if cnt == n - 1 else float("inf")

        # Get MST base weight
        base = kruskal(-1, -1)

        critical = []
        pseudo = []

        for i in range(len(edges)):
            w1 = kruskal(i, -1)
            if w1 > base:
                critical.append(edges[i][3])
            else:
                w2 = kruskal(-1, i)
                if w2 == base:
                    pseudo.append(edges[i][3])

        return [critical, pseudo]
