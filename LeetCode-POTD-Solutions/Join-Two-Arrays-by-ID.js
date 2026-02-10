/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const map = new Map();

    // Add all objects from arr1 into the map
    for (const obj of arr1) {
        map.set(obj.id, { ...obj });
    }

    // Merge or add from arr2
    for (const obj of arr2) {
        if (map.has(obj.id)) {
            Object.assign(map.get(obj.id), obj);
        } else {
            map.set(obj.id, { ...obj });
        }
    }

    // Return sorted array by id
    return Array.from(map.values()).sort((a, b) => a.id - b.id);
};
