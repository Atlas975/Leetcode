#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, ceil(max(quantities) / (n // len(quantities)))
        while l < r:
            m = l + (r - l) // 2
            if sum(ceil(q / m) for q in quantities) > n:
                l = m + 1
            else:
                r = m
        return l


# @lc code=end
