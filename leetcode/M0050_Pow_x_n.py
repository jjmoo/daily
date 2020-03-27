class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, i):
            if 0 == i: return 1
            if 1 == i: return x
            half = pow(x, i // 2)
            return half * half * (1 if i & 1 == 0 else x)
        if n < 0: x, n = 1 / x, -n
        return pow(x, n)

    def myPowLoop(self, x: float, n: int) -> float:
        if n < 0: x, n = 1 / x, -n
        mask, result = 1, 1
        while mask <= n: mask <<= 1
        mask >>= 1
        while mask > 0:
            result *= result
            if n & mask: result *= x
            mask >>= 1
        return result

    def myPowLoop2(self, x: float, n: int) -> float:
        if n < 0: x, n = 1 / x, -n
        mask, result, current = 1, 1, x
        while mask <= n:
            if n & mask: result *= current
            current *= current
            mask <<= 1
        return result


test = Solution().myPowLoop2
print(1024, test(2, 10))
print(9.261, test(2.1, 3))
print(0.25, test(2, -2))


# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/powx-n
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
