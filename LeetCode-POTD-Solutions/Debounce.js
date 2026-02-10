/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer;

    return function(...args) {
        clearTimeout(timer);            // cancel previous timer
        timer = setTimeout(() => {      // reset timer
            fn(...args);                // execute after 't' ms
        }, t);
    };
};

/**
 * Example:
 * const log = debounce(console.log, 100);
 * log("Hello"); 
 * log("Hello"); 
 * log("Hello");
 * // Only logs "Hello" once — 100ms after the last call
 */
