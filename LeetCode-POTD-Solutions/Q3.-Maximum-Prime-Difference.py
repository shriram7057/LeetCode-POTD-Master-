class Solution(object):
    def maximumPrimeDifference(self, nums):

        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        first = -1
        last = -1

        for i in range(len(nums)):
            if isPrime(nums[i]):
                first = i
                break

        for i in range(len(nums)-1, -1, -1):
            if isPrime(nums[i]):
                last = i
                break

        return last - first
