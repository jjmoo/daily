from T0227_Basic_Calculator_II import Solution as Basic_Calculator

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return Basic_Calculator().calculate(s)


print(2, Solution().calculate('1 + 1'))
print(3, Solution().calculate(' 2-1 + 2 '))
print(23, Solution().calculate('(1+(4+5+2)-3)+(6+8)'))


# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# Example 1:

# Input: "1 + 1"
# Output: 2
# Example 2:

# Input: " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
