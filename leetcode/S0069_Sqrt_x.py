class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        result, value = x, x // 2
        while result > value:
            result, value = value, (value + x // value) // 2
        return result


test = Solution().mySqrt
print(2, test(4))
print(2, test(8))
print(0, test(0))
print(1, test(1))
print(1, test(99999999))


# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the value is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
