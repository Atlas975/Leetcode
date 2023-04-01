#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from collections import deque
from itertools import product


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        stack = deque([(x, y)])
        while stack:
            x, y = stack.pop()
            dxmin, dxmax = max(0, x - 1), min(n, x + 2)
            dymin, dymax = max(0, y - 1), min(m, y + 2)

            mines = sum(
                board[dx][dy] == "M" for dx, dy in product(range(dxmin, dxmax), range(dymin, dymax))
            )

            if mines > 0:
                board[x][y] = str(mines)
                continue

            board[x][y] = "B"
            stack.extend(
                (dx, dy)
                for dx, dy in product(range(dxmin, dxmax), range(dymin, dymax))
                if board[dx][dy] == "E"
            )

        return board


# @lc code=end
