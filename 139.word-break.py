#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#


# @lc code=start

from collections import defaultdict, deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ns = len(s)
        dp = [False] * (ns + 1)
        dp[-1] = True

        wordmp = defaultdict(set)
        for w in wordDict:
            wordmp[len(w)].add(w)

        for i in reversed(range(ns)):
            for wlen in wordmp:
                if (i + wlen > ns) or (s[i : i + wlen] not in wordmp[wlen]):
                    continue
                dp[i] = dp[i + wlen]
                if dp[i]:
                    break
        return dp[0]


# @lc code=end
