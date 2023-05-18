#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start


from itertools import product


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # ITERATIVE
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i, j in product(range(1, n1 + 1), range(1, n2 + 1)):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

        # RECURSIVE
        # n1, n2 = len(text1), len(text2)
        # dp = [[None] * (n2 + 1) for _ in range(n1 + 1)]

        # def helper(r, c) -> int:
        #     if dp[r][c] is not None:
        #         return dp[r][c]

        #     if r < 0 or c < 0:
        #         return 0
        #     if text1[r] == text2[c]:
        #         dp[r][c] = helper(r - 1, c - 1) + 1
        #         return dp[r][c]
        #     dp[r][c] = max(helper(r - 1, c), helper(r, c - 1))
        #     return dp[r][c]

        # return helper(len(text1) - 1, len(text2) - 1)


# @lc code=end
