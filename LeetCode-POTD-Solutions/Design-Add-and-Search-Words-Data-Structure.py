class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            c = word[i]
            if c == '.':
                for nxt in node:
                    if nxt != '#' and dfs(i + 1, node[nxt]):
                        return True
                return False
            if c not in node:
                return False
            return dfs(i + 1, node[c])

        return dfs(0, self.trie)
