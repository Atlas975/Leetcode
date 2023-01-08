#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from itertools import product


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def capture(r, c):
            if board[r][c] != "O":
                return
            board[r][c] = "C"
            capture(r - 1, c) if r else None
            capture(r + 1, c) if r < n - 1 else None
            capture(r, c - 1) if c else None
            capture(r, c + 1) if c < m - 1 else None

        for r in range(n):
            capture(r, 0)
            capture(r, m - 1)

        for c in range(m):
            capture(0, c)
            capture(n - 1, c)

        for r, c in product(range(n), range(m)):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "C":
                board[r][c] = "O"


# @lc code=end
