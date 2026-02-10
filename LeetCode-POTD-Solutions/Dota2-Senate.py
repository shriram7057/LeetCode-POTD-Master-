from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        r_q = deque()
        d_q = deque()
        n = len(senate)

        # Put indices into respective queues
        for i, ch in enumerate(senate):
            if ch == 'R':
                r_q.append(i)
            else:
                d_q.append(i)

        # Simulate rounds
        while r_q and d_q:
            r = r_q.popleft()
            d = d_q.popleft()

            # The smaller index bans the other
            if r < d:
                r_q.append(r + n)
            else:
                d_q.append(d + n)

        return "Radiant" if r_q else "Dire"
