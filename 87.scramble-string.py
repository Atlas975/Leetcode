#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from typing import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)


# @lc code=end
