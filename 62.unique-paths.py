#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from itertools import product
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP SOLUTION
        dp = [1] * m
        for x, y in product(range(1, n), range(1, m)):
            dp[y] += dp[y - 1]
        return dp[-1]
    
        # COMBINATORICS SOLUTION
        return comb(m + n - 2, m - 1)

# @lc code=end
