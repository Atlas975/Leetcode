#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = l = 0
        for r, cur in enumerate(prices[1:], start=1):
            if cur > prices[l]:
                profit = max(profit, cur - prices[l])
            else:
                l = r
        return profit


# @lc code=end
