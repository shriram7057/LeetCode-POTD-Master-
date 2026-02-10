class Calculator {
    constructor(value) {
        this.result = value;
    }

    add(num) {
        this.result += num;
        return this;
    }

    subtract(num) {
        this.result -= num;
        return this;
    }

    multiply(num) {
        this.result *= num;
        return this;
    }

    divide(num) {
        if (num === 0) throw new Error("Division by zero is not allowed");
        this.result /= num;
        return this;
    }

    power(num) {
        this.result = Math.pow(this.result, num);
        return this;
    }

    getResult() {
        return this.result;
    }
}
