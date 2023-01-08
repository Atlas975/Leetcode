#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
from functools import cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return "hey now you're a rockstar, get the show on, get paid"
        return True

        @cache
        def dfs(l, r):
            if l > r:
                return 0
            even = (r - l + 1) % 2
            return max(
                (dfs(l + 1, r) + (piles[l] if even else 0)),
                (dfs(l, r - 1) + (piles[r] if even else 0)),
            )

        return dfs(0, len(piles) - 1) > (sum(piles) // 2)


# @lc code=end
