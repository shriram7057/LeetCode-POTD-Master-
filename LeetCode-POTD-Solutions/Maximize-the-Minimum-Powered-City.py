class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        n = len(stations)
        
        # Prefix sum for initial power
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        
        # Function to compute total power at city i
        def get_power(i):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            return prefix[right] - prefix[left]
        
        # Check if we can achieve minimum power = mid
        def can(mid):
            added = [0] * n
            extra = 0
            used = 0
            window_sum = 0
            
            for i in range(n):
                if i - r - 1 >= 0:
                    window_sum -= added[i - r - 1]
                if i + r < n:
                    window_sum += stations[i + r] if i + r < n else 0
                total = get_power(i) + extra
                if total < mid:
                    need = mid - total
                    used += need
                    if used > k:
                        return False
                    pos = min(n - 1, i + r)
                    added[pos] += need
                    extra += need
            return True

        # Binary search for maximum minimum power
        lo, hi = 0, 10**15
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canAchieve(stations, r, k, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def canAchieve(self, stations, r, k, mid):
        n = len(stations)
        added = [0] * n
        total = [0] * n
        window = 0
        for i in range(min(r, n)):
            window += stations[i]
        res = 0
        for i in range(n):
            if i + r < n:
                window += stations[i + r]
            total[i] = window
            if i - r >= 0:
                window -= stations[i - r]
        used = 0
        curAdd = 0
        diff = [0] * (n + 1)
        for i in range(n):
            curAdd += diff[i]
            total[i] += curAdd
            if total[i] < mid:
                need = mid - total[i]
                used += need
                if used > k:
                    return False
                total[i] += need
                curAdd += need
                if i + 2 * r + 1 < n:
                    diff[i + 2 * r + 1] -= need
        return True
