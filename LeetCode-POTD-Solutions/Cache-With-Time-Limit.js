/**
 * @param {number} ttl
 */
var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exists = this.cache.has(key);

    if (exists) clearTimeout(this.cache.get(key).timeout);

    const timeout = setTimeout(() => this.cache.delete(key), duration);
    this.cache.set(key, { value, timeout });

    return exists;
};

/** 
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.cache.has(key) ? this.cache.get(key).value : -1;
};

/** 
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};

/**
 * Example usage:
 * const cache = new TimeLimitedCache();
 * cache.set(1, 42, 1000); // false
 * cache.get(1);           // 42
 * cache.count();          // 1
 */
