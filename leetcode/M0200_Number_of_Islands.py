from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        from collections import deque
        def check(queue, i, j):
            if 0 <= i and i < n and 0 <= j and j < m and '1' == grid[i][j] and not memo[i][j]:
                memo[i][j] = True
                queue.append((i, j))
        result, n, m = 0, len(grid), len(grid[0])
        memo = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if '1' == grid[i][j] and not memo[i][j]:
                    result += 1
                    memo[i][j] = True
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        k, l = queue.popleft()
                        check(queue, k - 1, l)
                        check(queue, k + 1, l)
                        check(queue, k, l - 1)
                        check(queue, k, l + 1)
        return result

    def numIslandsInplace(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        from collections import deque
        result, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if '1' == grid[i][j]:
                    result += 1
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        k, l = queue.popleft()
                        if k > 0 and '1' == grid[k - 1][l]:
                            grid[k - 1][l] = '0'
                            queue.append((k - 1, l))
                        if l > 0 and '1' == grid[k][l - 1]:
                            grid[k][l - 1] = '0'
                            queue.append((k, l - 1))
                        if k < n - 1 and '1' == grid[k + 1][l]:
                            grid[k + 1][l] = '0'
                            queue.append((k + 1, l))
                        if l < m - 1 and '1' == grid[k][l + 1]:
                            grid[k][l + 1] = '0'
                            queue.append((k, l + 1))
        return result


test = Solution().numIslandsInplace
print(1, test([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]))
print(3, test([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]))


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
