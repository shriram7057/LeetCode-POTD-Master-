class Solution(object):
    def mostBooked(self, n, meetings):
        import heapq

        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)

        busy = []
        count = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + duration, room))

            count[room] += 1

        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
