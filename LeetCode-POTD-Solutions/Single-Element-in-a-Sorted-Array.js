1var singleNonDuplicate = function(nums) {
2    let left = 0, right = nums.length - 1;
3
4    while (left < right) {
5        let mid = Math.floor((left + right) / 2);
6
7        // ensure mid is even
8        if (mid % 2 === 1) mid--;
9
10        if (nums[mid] === nums[mid + 1]) {
11            left = mid + 2;
12        } else {
13            right = mid;
14        }
15    }
16
17    return nums[left];
18};
19