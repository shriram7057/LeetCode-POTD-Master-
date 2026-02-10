class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import deque, defaultdict
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(L):
                patterns[word[:i] + "*" + word[i+1:]].append(word)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                for nxt in patterns[pat]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
                patterns[pat] = []
        return 0
