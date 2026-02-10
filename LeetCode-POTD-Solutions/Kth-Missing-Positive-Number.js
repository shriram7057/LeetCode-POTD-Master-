1var findKthPositive = function(arr, k) {
2    let left = 0, right = arr.length - 1;
3
4    while (left <= right) {
5        let mid = Math.floor((left + right) / 2);
6        let missing = arr[mid] - (mid + 1);
7
8        if (missing < k) {
9            left = mid + 1;
10        } else {
11            right = mid - 1;
12        }
13    }
14
15    return left + k;
16};
17