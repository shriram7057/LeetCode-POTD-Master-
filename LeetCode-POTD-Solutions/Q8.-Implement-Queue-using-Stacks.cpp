#include <stack>
using namespace std;

class MyQueue {
public:
    stack<int> inStack, outStack;

    MyQueue() {}

    void push(int x) {
        inStack.push(x);
    }

    int pop() {
        peek(); // ensure outStack has the current front element
        int val = outStack.top();
        outStack.pop();
        return val;
    }

    int peek() {
        if (outStack.empty()) {
            while (!inStack.empty()) {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }
        return outStack.top();
    }

    bool empty() {
        return inStack.empty() && outStack.empty();
    }
};
