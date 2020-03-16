class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        size = len(board)
        half, raw_sum, col_sum = size >> 1, 0, 0
        for i in range(size):
            raw_sum += board[0][i]
            col_sum += board[i][0]
        if size & 1 == 0:
            if raw_sum != half or col_sum != half:
                return -1
        elif raw_sum != half and raw_sum != half + 1:
            return -1
        elif col_sum != half and col_sum != half + 1:
            return -1
        for i in range(1, size):
            for j in range(1, size):
                if board[i][j] != board[0][0] ^ board[i][0] ^ board[0][j]:
                    return -1
        step_raw, step_col = 0, 0
        if size & 1 == 0:
            raw_ref, col_ref = board[0][0], board[0][0]
        else:
            raw_ref = 0 if raw_sum == half else 1
            col_ref = 0 if col_sum == half else 1
        for i in range(0, size):
            if board[0][i] != (i & 1) ^ raw_ref:
                step_raw += 1
            if board[i][0] != (i & 1) ^ col_ref:
                step_col += 1
        if size & 1 == 0:
            step_raw = min(step_raw, size - step_raw)
            step_col = min(step_col, size - step_col)
        return (step_raw + step_col) // 2


print(Solution().movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))
print(Solution().movesToChessboard([[0, 1], [1, 0]]))
print(Solution().movesToChessboard([[1, 0], [1, 0]]))
print(Solution().movesToChessboard([[0, 0, 1], [1, 1, 0], [1, 1, 0]]))
print(Solution().movesToChessboard([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))
print(Solution().movesToChessboard([[0,0,1,0,1,1],[1,1,0,1,0,0],[1,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,1,0,1,1]]))


# An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

# What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

# Examples:
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation:
# One potential sequence of moves is shown below, from left to right:

# 0110     1010     1010
# 0110 --> 1010 --> 0101
# 1001     0101     1010
# 1001     0101     0101

# The first move swaps the first and second column.
# The second move swaps the second and third row.


# Input: board = [[0, 1], [1, 0]]
# Output: 0
# Explanation:
# Also note that the board with 0 in the top left corner,
# 01
# 10

# is also a valid chessboard.

# Input: board = [[1, 0], [1, 0]]
# Output: -1
# Explanation:
# No matter what sequence of moves you make, you cannot end with a valid chessboard.
# Note:

# board will have the same number of rows and columns, a number in the range [2, 30].
# board[i][j] will be only 0s or 1s.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/transform-to-chessboard
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
