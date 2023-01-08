#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
from collections import deque


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = deque()
        for i, price in enumerate(prices):
            while s and prices[s[-1]] >= price:
                prices[s.pop()] -= price
            s.append(i)
        return prices


# @lc code=end
