#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
from collections import deque


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # DYNAMIC PROGRAMMING
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]  # used when the substring extends to the end of s
        for l in reversed(range(n)):
            dp[l].extend([[s[l]] + sub2 for sub2 in dp[l + 1]])  # single char is a palindrome
            for r in range(l + 2, n + 1):
                sub1 = s[l:r]
                if all(sub1[k] == sub1[-k - 1] for k in range(len(sub1) // 2)):
                    dp[l].extend([sub1] + sub2 for sub2 in dp[r])
        return dp[0]

        # BACKTRACKING
        res, parts = [], []
        n = len(s)
        isPali = lambda arg: all(arg[1][k] == arg[1][-k - 1] for k in range(len(arg[1]) // 2))
        def dfs(i):
            for j, sub in filter(isPali, ((j, s[i : j + 1]) for j in range(i, n))):
                if j == len(s) - 1:
                    res.append(parts + [sub])
                else:
                    parts.append(sub)
                    dfs(j + 1)
                    parts.pop()
        dfs(0)
        return res



# @lc code=end
