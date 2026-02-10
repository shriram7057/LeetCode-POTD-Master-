class Solution:
    def minTime(self, ranks, n):
        # code here
        def donuts_in_time(time):
            total = 0
            for r in ranks:
                t = 0
                k = 1
                while t + k * r <= time:
                    t += k * r
                    total += 1
                    k += 1
                    if total >= n:
                        return True
            return total >= n
        low , high= 0,max(ranks)*n*(n+1)//2
        ans = high
        while low <= high:
            mid = (low+high)//2
            if donuts_in_time(mid):
                ans = mid 
                high = mid - 1
            else:
                low = mid+1
        return ans
               