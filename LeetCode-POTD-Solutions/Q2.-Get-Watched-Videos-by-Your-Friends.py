class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        from collections import deque, Counter

        n = len(friends)
        seen = [False] * n
        q = deque([id])
        seen[id] = True

        cur_level = 0
        while q and cur_level < level:
            for _ in range(len(q)):
                u = q.popleft()
                for v in friends[u]:
                    if not seen[v]:
                        seen[v] = True
                        q.append(v)
            cur_level += 1

        freq = Counter()
        while q:
            friend = q.popleft()
            for video in watchedVideos[friend]:
                freq[video] += 1

        return sorted(freq.keys(), key=lambda x: (freq[x], x))
