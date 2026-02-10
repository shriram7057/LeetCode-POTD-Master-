class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        from collections import deque

        bank = set(bank)
        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = set([startGene])
        chars = ["A", "C", "G", "T"]

        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for ch in chars:
                    if gene[i] != ch:
                        mutated = gene[:i] + ch + gene[i+1:]
                        if mutated in bank and mutated not in visited:
                            visited.add(mutated)
                            q.append((mutated, steps + 1))

        return -1
