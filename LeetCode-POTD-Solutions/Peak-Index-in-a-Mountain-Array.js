1var peakIndexInMountainArray = function(arr) {
2    let left = 0, right = arr.length - 1;
3
4    while (left < right) {
5        let mid = Math.floor((left + right) / 2);
6        if (arr[mid] < arr[mid + 1]) {
7            left = mid + 1;
8        } else {
9            right = mid;
10        }
11    }
12
13    return left;
14};
15