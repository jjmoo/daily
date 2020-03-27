from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: return 0
        result, lines, stack = [], [], []
        table = [[False] * n for _ in range(n)]
        for i in range(n):
            lines.append('.' * i + 'Q' + '.' * (n - 1 - i))
        def backtrack(i = 0):
            nonlocal result
            choice = []
            for j in range(n):
                if not table[i][j]: choice.append(j)
            if i >= n - 1:
                if choice:
                    stack.append(lines[choice[0]])
                    result.append(list(stack))
                    stack.pop()
                return
            for j in choice:
                changed = []
                for k in range(i + 1, n):
                    if i + j - k >= 0 and not table[k][i + j - k]:
                        table[k][i + j - k] = True
                        changed.append((k, i + j - k))
                    if not table[k][j]:
                        table[k][j] = True
                        changed.append((k, j))
                    if j - i + k < n and not table[k][j - i + k]:
                        table[k][j - i + k] = True
                        changed.append((k, j - i + k))
                stack.append(lines[j])
                backtrack(i + 1)
                stack.pop()
                for k, l  in changed:
                    table[k][l] = False
        backtrack()
        return result


test = Solution().solveNQueens
print(test(8))


# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/n-queens
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
