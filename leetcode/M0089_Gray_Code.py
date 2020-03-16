from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(2 ** n):
            val = 0
            for j in range(n):
                # bit 0: 0 1-1 0-0 1-1 0-0 1-1 0-0 1-1 0
                # bit 1: 0-0 1-1-1-1 0-0-0-0 1-1-1-1 0-0
                # bit 2: 0-0-0-0 1-1-1-1-1-1-1-1 0-0-0-0
                x = (i % 2 ** (j + 2)) // (2 ** j)
                val += (1 << j) if 1 <= x and x < 3 else 0
            result.append(val)
        return result

    def grayCodeMirror(self, n: int) -> List[int]:
        head, result = 1, [0]
        for _ in range(n):
            for j in range(len(result) - 1, -1, -1):
                result.append(head + result[j])
            head <<= 1
        return result


test = Solution().grayCodeMirror
print(test(4))
print(test(0))

# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

# Example 1:

# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.

# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/gray-code
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
