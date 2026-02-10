class NumArray(object):

    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.arr = nums[:]

        def add(i, val):
            while i <= self.n:
                self.bit[i] += val
                i += i & -i

        for i, v in enumerate(nums):
            add(i + 1, v)

    def update(self, index, val):
        diff = val - self.arr[index]
        self.arr[index] = val

        i = index + 1
        while i <= self.n:
            self.bit[i] += diff
            i += i & -i

    def sumRange(self, left, right):
        def psum(i):
            s = 0
            while i > 0:
                s += self.bit[i]
                i -= i & -i
            return s

        return psum(right + 1) - psum(left)
