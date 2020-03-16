class Solution(object):
    __ops = {
        '(': (0, None), ')': (0, None), 
        '+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y), 
        '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x // y)}

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [('(', 0)]
        def expr(value, level=None):
            if level is not None and value is not '(':
                while stack[-2][1] >= level:
                    if stack[-2][0] is '(':
                        stack[-1] = stack.pop()[0], None
                        return
                    else:
                        num2 = stack.pop()[0]
                        op_cur = stack.pop()[0]
                        stack[-1] = self.__ops[op_cur][1](stack[-1][0], num2), None
            if value is not None:
                stack.append((value, level))
        num = None
        for ch in s:
            if ch.isdigit():
                num = int(ch) if num is None else int(ch) + num * 10
            elif ch in self.__ops:
                expr(num)
                expr(ch, self.__ops[ch][0])
                num = None
        expr(num)
        expr(')', 0)
        return stack[0][0]


print(7, Solution().calculate('3+2*2'))
print(1, Solution().calculate(' 3/2 '))
print(5, Solution().calculate(' 3+5 / 2 '))
print(10, Solution().calculate(' 3+1 5 / 2 '))
print(4, Solution().calculate('3+15/(2+ 4*(5/3+1))'))


# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:

# Input: "3+2*2"
# Output: 7
# Example 2:

# Input: " 3/2 "
# Output: 1
# Example 3:

# Input: " 3+5 / 2 "
# Output: 5
# Note:

# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
