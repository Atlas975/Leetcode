#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            time = sum((ceil(p / k)) for p in piles)
            if time > h:
                lo = k + 1
            else:
                hi = k
        return hi


# @lc code=end
