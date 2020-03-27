from typing import List
from M0054_Spiral_Matrix import walkAround

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0: return [[]]
        result = [[0] * n for _ in range(n)]
        for k, (i, j) in enumerate(walkAround(result), 1):
            result[i][j] = k
        return result


test = Solution().generateMatrix
for l in test(5): print(l)


# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/spiral-matrix-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
