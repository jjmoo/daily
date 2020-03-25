from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num < 0: return []
        result = [0] * (num + 1)
        def countRight(x):
            x, cnt = x & (-x), 0
            while x > 1:
                x >>= 1
                cnt += 1
            return cnt
        for i in range(1, num + 1):
            if i & 1:
                result[i] = result[i - 1] + 1
            else:
                result[i] = result[i - 1] + 1 - countRight(i)
        return result

    def countBits2(self, num: int) -> List[int]:
        if num < 0: return []
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result

    def countBits3(self, num: int) -> List[int]:
        if num < 0: return []
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i & i - 1] + 1
        return result


test = Solution().countBits3
print(test(10))


# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/counting-bits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
