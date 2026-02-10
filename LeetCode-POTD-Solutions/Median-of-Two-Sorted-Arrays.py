class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)

        if m > n:
            A, B, m, n = B, A, n, m

        total = m + n
        half = total // 2

        l, r = 0, m
        while True:
            i = (l + r) // 2
            j = half - i

            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
