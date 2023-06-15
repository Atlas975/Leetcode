#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from collections import defaultdict
from itertools import chain, product


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(r, c, val):
            for i in range(9):
                if val in (board[i][c], board[r][i]):
                    return False
            for i, j in product(range(3), range(3)):
                if board[(r // 3) * 3 + i][(c // 3) * 3 + j] == val:
                    return False
            return True
        # cols, rows, grid = defaultdict(set), defaultdict(set), defaultdict(set)

        # for r, c in product(range(9), range(9)):
        #     if (tile := board[r][c]) != ".":
        #         cols[c].add(tile)
        #         rows[r].add(tile)
        #         grid[r // 3, c // 3].add(tile)

        # empty = [(r, c) for r, c in product(range(9), range(9)) if board[r][c] == "."]

        # def valid_insert(r, c, val):
        #     for i in range(9):
        #         col = board[i][c]
        #         row = board[r][i]
        #         grid = board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3]
        #         if col != "." and col == val:
        #             return False
        #         if row != "." and row == val:
        #             return False
        #         if grid != "." and grid == val:
        #             return False
        #     return True

        # while empty:
        #     for r, c in list(empty):
        #         for strnum in map(str, range(1, 10)):
        #             if valid_insert(r, c, strnum):
        #                 board[r][c] = strnum
        #                 empty.remove((r, c))
        #                 break

        """
        Do not return anything, modify board in-place instead.
        """


# @lc code=end
