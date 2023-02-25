#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
from functools import cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dfs(l, m, turn):
            if l + 2 * m >= n:
                return sum(piles[l:]) if turn else 0

            return (
                max(sum(piles[l : l + x]) + dfs(l + x, max(m, x), 0) for x in range(1, 2 * m + 1))
                if turn
                else min(dfs(l + x, max(m, x), 1) for x in range(1, 2 * m + 1))
            )

        return dfs(0, 1, 1)


# @lc code=end
