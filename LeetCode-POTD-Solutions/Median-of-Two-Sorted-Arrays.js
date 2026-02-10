1var findMedianSortedArrays = function(nums1, nums2) {
2    if (nums1.length > nums2.length) {
3        return findMedianSortedArrays(nums2, nums1);
4    }
5
6    let m = nums1.length, n = nums2.length;
7    let left = 0, right = m;
8
9    while (left <= right) {
10        let i = Math.floor((left + right) / 2);
11        let j = Math.floor((m + n + 1) / 2) - i;
12
13        let maxLeftA = (i === 0) ? -Infinity : nums1[i - 1];
14        let minRightA = (i === m) ? Infinity : nums1[i];
15
16        let maxLeftB = (j === 0) ? -Infinity : nums2[j - 1];
17        let minRightB = (j === n) ? Infinity : nums2[j];
18
19        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
20            if ((m + n) % 2 === 0) {
21                return (Math.max(maxLeftA, maxLeftB) + Math.min(minRightA, minRightB)) / 2;
22            } else {
23                return Math.max(maxLeftA, maxLeftB);
24            }
25        } else if (maxLeftA > minRightB) {
26            right = i - 1;
27        } else {
28            left = i + 1;
29        }
30    }
31};
32