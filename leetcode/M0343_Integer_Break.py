class Solution(object):
    saved = [0] * 60
    index = -1

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= self.index:
            return self.saved[self.index]
        else:
            if self.index <= 2:
                self.saved[0] = 1
                self.saved[1] = 1
                self.saved[2] = 1
                self.index = 2
            for i in range(self.index + 1, n + 1):
                result = 1
                for j in range(1, i // 2 + 1):
                    value = max(j, self.saved[j]) * max(i - j, self.saved[i - j])
                    result = max(result, value)
                self.saved[i] = result
            self.index = max(self.index, n)
            return self.saved[n]

print(Solution().integerBreak(10))
print(Solution().integerBreak(58))


# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# Example 1:

# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/integer-break
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
