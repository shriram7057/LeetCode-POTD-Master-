class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ans = 1
        for i in range(len(points)):
            slopes = {}
            same = 0
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue

                dx = x2 - x1
                dy = y2 - y1
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1

            max_line = max(slopes.values()) if slopes else 0
            ans = max(ans, max_line + same + 1)

        return ans
