class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mini or x <= self.mini[-1]:
            self.mini.append(x)

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            if self.mini[-1] == top:
                self.mini.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]

    def getMin(self) -> int:
        if self.mini: return self.mini[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(-3, minStack.getMin())
minStack.pop()
print(0, minStack.top())
print(-2, minStack.getMin())


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
