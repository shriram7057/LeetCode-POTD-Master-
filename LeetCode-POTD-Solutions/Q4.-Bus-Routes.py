class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        from collections import deque, defaultdict

        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, r in enumerate(routes):
            for stop in r:
                stop_to_routes[stop].append(i)

        q = deque([source])
        visited_stops = set([source])
        visited_routes = set()
        buses = 0

        while q:
            buses += 1
            for _ in range(len(q)):
                stop = q.popleft()
                for route in stop_to_routes[stop]:
                    if route in visited_routes:
                        continue
                    visited_routes.add(route)
                    for next_stop in routes[route]:
                        if next_stop == target:
                            return buses
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append(next_stop)

        return -1
