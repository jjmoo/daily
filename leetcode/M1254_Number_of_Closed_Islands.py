from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        from collections import deque
        result, n, m = 0, len(grid), len(grid[0])
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if 0 == grid[i][j]:
                    grid[i][j] = 1
                    queue = deque()
                    queue.append((i, j))
                    valid = True
                    while queue:
                        l, k = queue.popleft()
                        for lo, ko in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            ll, kk = l + lo, k + ko
                            if 0 <= ll and ll < n and 0 <= kk and kk < m and 0 == grid[ll][kk]:
                                grid[ll][kk] = 1
                                queue.append((ll, kk))
                                if ll == 0 or ll == n - 1 or kk == 0 or kk == m - 1:
                                    valid = False
                    if valid:
                        result += 1
        return result

    def closedIsland2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        from collections import deque
        result, n, m = 0, len(grid), len(grid[0])
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if 0 == grid[i][j]:
                    grid[i][j] = 1
                    queue = deque()
                    queue.append((i, j))
                    valid = True
                    while queue:
                        l, k = queue.popleft()
                        for lo, ko in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            ll, kk = l + lo, k + ko
                            if 0 == grid[ll][kk]:
                                grid[ll][kk] = 1
                                if ll == 0 or ll == n - 1 or kk == 0 or kk == m - 1:
                                    valid = False
                                else:
                                    queue.append((ll, kk))
                    if valid:
                        result += 1
        return result


test = Solution().closedIsland2

gri1 = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]

gri2 = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]

gri3 = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]

gri4 = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]

gri5 = [[1,1,0,1,1,1,1,1,1,1],
        [0,0,1,0,0,1,0,1,1,1],
        [1,0,1,0,0,0,1,0,1,0],
        [1,1,1,1,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,0],
        [0,0,0,0,1,1,0,0,0,0],
        [1,0,1,0,0,0,0,1,1,0],
        [1,1,0,0,1,1,0,0,0,0],
        [0,0,0,1,1,0,1,1,1,0],
        [1,1,0,1,0,1,0,0,1,0]]

gri6 = [[1,0,1,1,1,1,0,0,1,0],
        [1,0,1,1,0,0,0,1,1,1],
        [0,1,1,0,0,0,1,0,0,0],
        [1,0,1,1,0,1,0,0,1,0],
        [0,1,1,1,0,1,0,1,0,0],
        [1,0,0,1,0,0,1,0,0,0],
        [1,0,1,1,1,0,0,1,1,0],
        [1,1,0,1,1,0,1,0,1,1],
        [0,0,1,1,1,0,1,0,1,1],
        [1,0,0,1,1,1,1,0,1,1]]

print(2, test(gri1))
print(1, test(gri2))
print(2, test(gri3))
print(5, test(gri4))
print(4, test(gri5))
print(3, test(gri6))


# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

# Example 1:

# Input: grid = [[1,1,1,1,1,1,1,0],
#                [1,0,0,0,0,1,1,0],
#                [1,0,1,0,1,1,1,0],
#                [1,0,0,0,0,1,0,1],
#                [1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
# Example 2:

# Input: grid = [[0,0,1,0,0],
#                [0,1,0,1,0],
#                [0,1,1,1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
#  

# Constraints:

# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-closed-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
