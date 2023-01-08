#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
from functools import cache
from itertools import product, starmap


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        @cache
        def dfs(r, c):
            cur = matrix[r][c]
            return 1 + max(
                dfs(r + 1, c) if r + 1 < n and matrix[r + 1][c] > cur else 0,
                dfs(r - 1, c) if r >= 1 and matrix[r - 1][c] > cur else 0,
                dfs(r, c + 1) if c + 1 < m and matrix[r][c + 1] > cur else 0,
                dfs(r, c - 1) if c >= 1 and matrix[r][c - 1] > cur else 0,
            )

        return max(starmap(dfs, product(range(n), range(m))))


# @lc code=end
