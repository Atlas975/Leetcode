#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
from collections import deque
from functools import cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # DYNAMIC PROGRAMMING (ITERATIVE)
        # n = len(s)
        # dp = [[] for _ in range(n + 1)]
        # dp[n] = [[]]  # used when the substring extends to the end of s
        # for l in reversed(range(n)):
        #     dp[l].extend([[s[l]] + sub2 for sub2 in dp[l + 1]])  # single char is a palindrome
        #     for r in range(l + 2, n + 1):
        #         sub1 = s[l:r]
        #         if all(sub1[k] == sub1[-k - 1] for k in range(len(sub1) // 2)):
        #             dp[l].extend([sub1] + sub2 for sub2 in dp[r])
        # return dp[0]

        # DYNAMIC PROGRAMMING (RECURSIVE)
        n = len(s)
        isPali = lambda x: all(x[k] == x[-k - 1] for k in range(len(x) // 2))

        @cache
        def dfs(l):
            if l == n:
                return [[]]
            dp = []
            dp.extend([[s[l]] + sub2 for sub2 in dfs(l + 1)])
            for r in range(l + 2, n + 1):
                lsub = s[l:r]
                if isPali(lsub):
                    dp.extend([[lsub] + rsub for rsub in dfs(r)])
            return dp

        return dfs(0)


# @lc code=end
