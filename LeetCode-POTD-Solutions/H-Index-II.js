1var hIndex = function(citations) {
2    const n = citations.length;
3    let left = 0, right = n - 1;
4
5    while (left <= right) {
6        const mid = Math.floor((left + right) / 2);
7        const h = n - mid;
8
9        if (citations[mid] >= h) {
10            right = mid - 1;   // try to find a smaller index
11        } else {
12            left = mid + 1;
13        }
14    }
15
16    return n - left;
17};
18