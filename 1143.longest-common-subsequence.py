#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from itertools import product
from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # ITERATIVE
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i, j in product(range(n1), range(n2)):
            a, b = text1[i], text2[j]
            dp[i + 1][j + 1] = dp[i][j] + 1 if a == b else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]

        # RECURSIVE
        @cache
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return helper(i - 1, j - 1) + 1
            else:
                return max(helper(i - 1, j), helper(i, j - 1))

        return helper(len(text1) - 1, len(text2) - 1)


# @lc code=end
