from T0227_Basic_Calculator_II import Solution as Basic_Calculator

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return Basic_Calculator().calculate(s)



print(7, Solution().calculate("3+2*2"))
print(1, Solution().calculate("3/2"))
print(5, Solution().calculate(" 3+5 / 2 "))


# Given an arithmetic equation consisting of positive integers, +, -, * and / (no paren­theses), compute the result.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:

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
# 链接：https://leetcode-cn.com/problems/calculator-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
