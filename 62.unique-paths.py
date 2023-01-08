#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            dp[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
            return dp[i][j]


# @lc code=end
