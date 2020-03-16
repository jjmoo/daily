from typing import List

def walkAround(matrix: List[List[int]], start = 0):
    n, m = len(matrix), len(matrix[0])
    min_start = min((n - 1) // 2, (m - 1) // 2)
    if start > min_start: return
    for j in range(start, m - start):
        yield start, j
    if start + 1 >= n - start: return
    for i in range(start + 1, n - start):
        yield i, m - start - 1
    if m - start - 2 <= start - 1: return
    for j in range(m - start - 2, start - 1, -1):
        yield n - start - 1, j
    for i in range(n - start -2, start, -1):
        yield i, start
    for p in walkAround(matrix, start + 1):
        yield p


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        result = []
        for i, j in walkAround(matrix): result.append(matrix[i][j])
        return result


test = Solution().spiralOrder
print([1,2,3,4,8,12,11,10,9,5,6,7], test([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/spiral-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
