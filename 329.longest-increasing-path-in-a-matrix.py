#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
from itertools import product, starmap


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[None] * m for _ in range(n)]

        def dfs(r, c, prev=float("-inf")):
            if prev >= matrix[r][c]:
                return 0
            if dp[r][c]:
                return dp[r][c]
            dp[r][c] = 1 + max(
                dfs(r + 1, c, matrix[r][c]) if r < n - 1 else 0,
                dfs(r - 1, c, matrix[r][c]) if r > 0 else 0,
                dfs(r, c + 1, matrix[r][c]) if c < m - 1 else 0,
                dfs(r, c - 1, matrix[r][c]) if c > 0 else 0,
            )
            return dp[r][c]

        return max(starmap(dfs, product(range(n), range(m))))


# @lc code=end
