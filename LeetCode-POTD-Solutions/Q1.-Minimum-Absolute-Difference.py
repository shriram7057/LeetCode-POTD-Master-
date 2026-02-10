class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        minDiff = float('inf')
        res = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < minDiff:
                minDiff = diff
                res = [[arr[i-1], arr[i]]]
            elif diff == minDiff:
                res.append([arr[i-1], arr[i]])

        return res
