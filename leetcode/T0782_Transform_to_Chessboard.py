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
