#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from collections import Counter
from itertools import chain, product, starmap


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, wrdlen = len(board), len(board[0]), len(word)
        if wrdlen > m * n:
            return False

        def dfs(r, c, i=0) -> bool:
            if board[r][c] != word[i]:
                return False
            if i == wrdlen - 1:
                return True
            
            board[r][c] = "#"
            i += 1
            valid = (
                (r > 0 and dfs(r - 1, c, i))
                or (r < n - 1 and dfs(r + 1, c, i))
                or (c > 0 and dfs(r, c - 1, i))
                or (c < m - 1 and dfs(r, c + 1, i))
            )
            board[r][c] = word[i - 1]
            return valid

        wordcnt, boardcnt = Counter(word), Counter(chain(*board))
        if any(wordcnt[c] > boardcnt[c] for c in wordcnt):
            return False
        if wordcnt[word[0]] > wordcnt[word[-1]]:
            word = word[::-1]
        return any(starmap(dfs, product(range(n), range(m))))

# @lc code=end
