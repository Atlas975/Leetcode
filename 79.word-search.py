#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        wrdlen = len(word)
        if wrdlen > m * n:
            return False

        def bfs(r, c, idx):
            if idx == wrdlen - 1:
                return True
            board[r][c] = None
            valid = any(
                bfs(r + dr, c + dc, idx + 1)
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
                if n > r + dr >= 0
                and m > c + dc >= 0
                and board[r + dr][c + dc] == word[idx + 1]
            )
            board[r][c] = word[idx]
            return valid

        return any(
            bfs(r, c, 0)
            for r, c in product(range(n), range(m))
            if board[r][c] == word[0]
        )


# @lc code=end
