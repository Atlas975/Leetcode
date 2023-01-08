#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t) - Counter(s)).values())
        # sc = Counter(s)
        # res = 0
        # for c in t:
        #     if c in sc:
        #         sc[c] -= 1
        #         if sc[c] == 0:
        #             del sc[c]
        #     else:
        #         res += 1
        # return res


# @lc code=end
