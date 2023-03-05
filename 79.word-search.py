#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from collections import Counter
from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, wrdlen = len(board), len(board[0]), len(word)
        if wrdlen > m * n:
            return False

        def dfs(r, c, i=0):
            if i == wrdlen - 1:
                return True
            board[r][c] = "#"
            i, ch = i + 1, word[i + 1]
            valid = (
                (r > 0 and board[r - 1][c] == ch and dfs(r - 1, c, i))
                or (r < n - 1 and board[r + 1][c] == ch and dfs(r + 1, c, i))
                or (c > 0 and board[r][c - 1] == ch and dfs(r, c - 1, i))
                or (c < m - 1 and board[r][c + 1] == ch and dfs(r, c + 1, i))
            )
            board[r][c] = word[i - 1]
            return valid

        cnts = sum(map(Counter, board), Counter())
        if cnts[word[0]] > cnts[word[-1]]:
            word = word[::-1]
        return any(dfs(r, c) for r, c in product(range(n), range(m)) if board[r][c] == word[0])


# @lc code=end
