#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
from functools import cache


class Solution:
    def minCut(self, s: str) -> int:
        # P = set()
        # # P is the set of starting positions of palindromes ending at j

        # n = len(s)
        # pl = list(range(n + 1))  # pl[i+1] is the palindrome length of s[0:i] and pl[0] = 0

        # for j in range(n):

        #     # #find palindromes obtained by adding char at each end
        #     Q = {i - 1 for i in P if (i > 0 and s[i - 1] == s[j])}
        #     # find palindromes of length 2 obtained by adding 1 char
        #     if j > 0 and s[j - 1] == s[j]:
        #         Q.add(j - 1)

        #     Q.add(j)
        #     P = Q

        #     for i in P:
        #         pl[j + 1] = min(pl[j + 1], pl[i] + 1)
        # return pl[-1] - 1

        # n = len(s)
        # dp = [float("inf")] * (n + 1)
        # dp[-1] = 0

        # for l in reversed(range(n)):
        #     dp[l] = 1 + dp[l + 1]
        #     for r in range(l + 2, n + 1):
        #         sub = s[l:r]
        #         if sub == sub[::-1]:
        #             dp[l] = min(dp[l], 1 + dp[r])
        # return dp[0] - 1

        n = len(s)
        @cache
        def dfs(l):
            if l == n:
                return 0
            dp = 1 + dfs(l + 1)
            for r in range(l + 2, n + 1):
                sub = s[l:r]
                if sub == sub[::-1]:
                    dp = min(dp, 1 + dfs(r))
            return dp
        return dfs(0) - 1


# @lc code=end
