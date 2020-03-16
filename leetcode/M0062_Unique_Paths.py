class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)


test = Solution().uniquePaths
print(3, test(3, 2))
print(28, test(7, 3))


# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28
#  

# Constraints:

# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
