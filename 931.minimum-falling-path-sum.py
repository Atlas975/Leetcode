#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
from functools import cache


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int | float:

        n = len(matrix)

        @cache
        def dfs(r, c, res):
            if r == n:
                return 0
            elif c == n or c < 0:
                return float("inf")
            return matrix[r][c] + min(
                dfs(r + 1, c - 1, res),
                dfs(r + 1, c, res),
                dfs(r + 1, c + 1, res),
            )

        return min(dfs(0, c, 0) for c in range(n))


# @lc code=end
