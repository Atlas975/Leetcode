#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, buying):
            if i >= len(prices):
                return 0
            if buying:
                return max(dp(i + 1, True), dp(i + 1, False) - prices[i])
            else:
                return max(dp(i + 1, False), dp(i + 2, True) + prices[i])

        return dp(0, True)


# @lc code=end
