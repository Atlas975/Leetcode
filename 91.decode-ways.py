#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        # ITERATIVE
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            dp[i] = dp[i + 1]
            if i < n - 1 and int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]

        # RECURSIVE
        @cache
        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i < n - 1 and int(s[i : i + 2]) <= 26:
                res += dfs(i + 2)
            return res

        return dfs(0)


# @lc code=end
