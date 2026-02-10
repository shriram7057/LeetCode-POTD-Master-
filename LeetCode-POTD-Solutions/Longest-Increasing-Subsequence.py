class Solution(object):
    def lengthOfLIS(self, nums):
        import bisect
        lis = []
        for n in nums:
            i = bisect.bisect_left(lis, n)
            if i == len(lis):
                lis.append(n)
            else:
                lis[i] = n
        return len(lis)
