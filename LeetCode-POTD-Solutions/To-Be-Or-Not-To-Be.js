/**
 * @param {any} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (otherVal) => {
            if (val !== otherVal) throw new Error("Not Equal");
            else return true;
        },
        notToBe: (otherVal) => {
            if (val === otherVal) throw new Error("Equal");
            else return true;
        }
    };
};

/**
 * Example:
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
