#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
from itertools import product


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        og new
         0  0:0
         1  1:0
         0  2:1
         1  3:1

        """
        n, m = len(board), len(board[0])
        count_neighbours = lambda r, c: (
            sum(
                0 <= nr < n and 0 <= nc < m and board[nr][nc] % 2
                for nr, nc in (
                    (r - 1, c - 1),
                    (r - 1, c),
                    (r - 1, c + 1),
                    (r, c - 1),
                    (r, c + 1),
                    (r + 1, c - 1),
                    (r + 1, c),
                    (r + 1, c + 1),
                )
            )
        )

        for r, c in product(range(n), range(m)):
            count = count_neighbours(r, c)
            if (board[r][c] == 1 and count in {2, 3}) or (board[r][c] == 0 and count == 3):
                board[r][c] |= 2

        for r, c in product(range(n), range(m)):
            board[r][c] >>= 1


# @lc code=end
