#
# @lc app=leetcode id=62 lang=python3``
#
# [62] Unique Paths
#

# @lc code=start
from itertools import product


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for x, y in product(range(1, m), range(1, n)):
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[-1][-1]


# @lc code=end
