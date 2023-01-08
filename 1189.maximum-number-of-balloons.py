#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = Counter(text)
        return min(
            letters["b"],
            letters["a"],
            letters["l"] // 2,
            letters["o"] // 2,
            letters["n"],
        )


# @lc code=end
