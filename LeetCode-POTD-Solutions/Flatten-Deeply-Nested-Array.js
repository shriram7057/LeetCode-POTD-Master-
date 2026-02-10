/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function(arr, n) {
    if (n === 0) return arr;

    const result = [];

    for (const item of arr) {
        if (Array.isArray(item)) {
            result.push(...flat(item, n - 1)); // recursive call
        } else {
            result.push(item);
        }
    }

    return result;
};
