#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
from functools import cache
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



        @cache
        def alive_cnt(r, c):
            cnt = 0
            lc, rc = c > 0, c < m - 1
            if r > 0:
                lo = board[r - 1]
                cnt += (lo[c] % 2) + (lc and lo[c - 1] % 2) + (rc and lo[c + 1] % 2)
            if r < n - 1:
                hi = board[r + 1]
                cnt += (hi[c] % 2) + (lc and hi[c - 1] % 2) + (rc and hi[c + 1] % 2)
            return cnt + (lc and board[r][c - 1] % 2) + (rc and board[r][c + 1] % 2)

        for r, c in product(range(n), range(m)):
            cnt = alive_cnt(r, c)
            if (board[r][c] == 1 and cnt in (2, 3)) or (board[r][c] == 0 and cnt == 3):
                board[r][c] += 2

        for r, c in product(range(n), range(m)):
            board[r][c] >>= 1


# @lc code=end
 