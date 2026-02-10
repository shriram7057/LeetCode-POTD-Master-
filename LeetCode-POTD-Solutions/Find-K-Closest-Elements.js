1var findClosestElements = function(arr, k, x) {
2    let left = 0, right = arr.length - k;
3
4    while (left < right) {
5        let mid = Math.floor((left + right) / 2);
6        if (x - arr[mid] > arr[mid + k] - x) {
7            left = mid + 1;
8        } else {
9            right = mid;
10        }
11    }
12
13    return arr.slice(left, left + k);
14};
15