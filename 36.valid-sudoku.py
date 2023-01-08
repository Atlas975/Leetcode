#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start

from itertools import product
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        cols, rows, grid = defaultdict(set), defaultdict(set), defaultdict(set)

        for r, c in product(range(9), repeat=2):
            tile = board[r][c]
            if tile == ".":
                continue
            if tile in (cols[c] | rows[r] | grid[r // 3, c // 3]):
                return False
            cols[c].add(tile)
            rows[r].add(tile)
            grid[r // 3, c // 3].add(tile)
        return True


# @lc code=end
