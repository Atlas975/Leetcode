#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
from functools import cache
from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        # # ITERATIVE
        # dp = [1] * (n + 1)
        # for i in range(2, n+1):
        #     dp[i] = sum(dp[j] * dp[i-j-1] for j in range(i))
        # return dp[-1]

        # # RECURSIVE
        # @cache
        # def fact(x):
        #     return 1 if x <= 1 else (x * fact(x - 1))
        # return fact(2 * n) // (fact(n) * fact(n + 1))
        

# @lc code=end
