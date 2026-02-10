/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((group, item) => {
        const key = fn(item);
        if (!group[key]) group[key] = [];
        group[key].push(item);
        return group;
    }, {});
};
