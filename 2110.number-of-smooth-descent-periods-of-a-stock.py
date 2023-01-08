#
# @lc app=leetcode id=2110 lang=python3
#
# [2110] Number of Smooth Descent Periods of a Stock
#

# @lc code=start
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = n = len(prices)
        l = 0
        for r in range(1, n):
            if prices[r - 1] - prices[r] == 1:
                res += r - l
            else:
                l = r
        return res


# @lc code=end
