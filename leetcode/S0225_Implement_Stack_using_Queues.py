class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()
        self.cnt = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.cnt += 1
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.cnt > 0:
            self.cnt -= 1
            for _ in range(self.cnt):
                self.queue.append(self.queue.popleft())
            return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.cnt > 0:
            return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return 0 == self.cnt


stack = MyStack()
stack.push(1)
stack.push(2)  
print(stack.top())
print(stack.pop())
stack.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()# Implement the following operations of a stack using queues.


# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:

# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-stack-using-queues
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
