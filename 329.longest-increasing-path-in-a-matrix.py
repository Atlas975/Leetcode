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
        dp = [[None] * m for _ in range(n)]

        def dfs(r, c, outbound=False, prev=float("-inf")):
            if outbound or prev >= matrix[r][c]:
                return 0
            if dp[r][c]:
                return dp[r][c]

            cur = matrix[r][c]
            dp[r][c] = 1 + max(
                dfs(r + 1, c, r == n - 1, cur),
                dfs(r - 1, c, r == 0, cur),
                dfs(r, c + 1, c == m - 1, cur),
                dfs(r, c - 1, c == 0, cur),
            )
            return dp[r][c]

        return max(starmap(dfs, product(range(n), range(m))))


# @lc code=end
