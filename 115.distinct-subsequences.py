#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # ITERATIVE
        sn, tn = len(s), len(t)
        if sn < tn:
            return 0
        dp = [1] + ([0] * tn)

        for i in range(sn - tn + 1):
            for j in range(tn):
                if s[i + j] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]
        
        # RECURSIVE
        @cache
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            include, skip = dfs(i + 1, j + 1), dfs(i + 1, j)
            if s[i] == t[j]:
                return include + skip
            return skip
        return dfs(0, 0)
    



# @lc code=end
