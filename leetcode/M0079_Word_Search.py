from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, l = len(board), len(board[0]), len(word)
        table = [[False] * m for _ in range(n)]
        def backtrace(i, j, k = 1):
            if k == l: return True
            choice = []
            if i - 1 >= 0 and not table[i - 1][j]: choice.append((i - 1, j))
            if i + 1 < n and not table[i + 1][j]: choice.append((i + 1, j))
            if j - 1 >= 0 and not table[i][j - 1]: choice.append((i, j - 1))
            if j + 1 < m and not table[i][j + 1]: choice.append((i, j + 1))
            for ci, cj in choice:
                if board[ci][cj] == word[k]:
                    table[ci][cj] = True
                    if backtrace(ci, cj, k + 1): return True
                    table[ci][cj] = False
            return False
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    table[i][j] = True
                    if backtrace(i, j): return True
                    table[i][j] = False
        return False


test = Solution().exist
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
print(True, test(board, 'ABCCED'))
print(True, test(board, 'SEE'))
print(False, test(board, 'ABCB'))
board = [["a","a"]]
print(False, test(board, 'aaa'))


# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#  

# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
