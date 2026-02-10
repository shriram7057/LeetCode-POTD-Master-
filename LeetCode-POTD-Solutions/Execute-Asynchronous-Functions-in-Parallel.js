/**
 * @param {Function[]} functions
 * @return {Promise}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let completed = 0;

        if (functions.length === 0) {
            resolve(results);
            return;
        }

        functions.forEach((fn, index) => {
            fn()
                .then((res) => {
                    results[index] = res;
                    completed++;
                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch(reject); // reject immediately if any promise fails
        });
    });
};

/**
 * Example:
 * const functions = [
 *   () => new Promise(res => setTimeout(() => res(1), 300)),
 *   () => new Promise(res => setTimeout(() => res(2), 200)),
 *   () => new Promise(res => setTimeout(() => res(3), 100))
 * ];
 *
 * promiseAll(functions).then(console.log); // [1, 2, 3] after ~300ms
 */
