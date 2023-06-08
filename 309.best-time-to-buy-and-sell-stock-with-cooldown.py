#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ITERATIVE O(1) SPACE
        nstck = twodaypre = 0 # wo/ stock held maxprof, 2 day pre maxprof wo/ stock
        stck = -prices[0] # w/ stock held maxprof

        for p in prices[1:]:
            tmp = nstck
            nstck = max(nstck, stck + p)  # sell
            stck = max(stck, twodaypre - p) # buy
            twodaypre = tmp
        return nstck

        # RECURSIVE O(N) SPACE
        @cache
        def dfs(i, stockheld):
            if i >= len(prices):
                return 0
            skip = dfs(i + 1, stockheld)

            if stockheld:
                sell = dfs(i + 2, False) + prices[i]
                return max(sell, skip)
            buy = dfs(i + 1, True) - prices[i]
            return max(buy, skip)
        return dfs(0, False)



# @lc code=end
å
