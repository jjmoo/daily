class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >=0 else -1
        x, y = x if sign > 0 else -x, 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        y *= sign
        return 0 if y < -2**31 or y > 2**31 else y


test = Solution().reverse
print(321, test(123))
print(-321, test(-123))
print(21, test(120))
print(-21, test(-120))


# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
