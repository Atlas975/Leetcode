#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
from collections import deque


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n + 1):
                word = s[l:r]
                if all(word[k] == word[-k - 1] for k in range(len(word) // 2)):
                    dp[l].extend([word] + each for each in dp[r])
        return dp[0]


# @lc code=end
