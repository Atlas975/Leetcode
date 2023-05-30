#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = {coin for coin in coins if coin <= amount}
        if len(coins) == 0:  # no coins needed if amt = 0, no coins available if amt > 0
            return 0 if amount == 0 else -1

        dp = [float("inf")] * (amount + 1)
        minc, maxc = min(coins), max(coins)
        dp[0], dp[minc], dp[maxc] = 0, 1, 1  
        for a in range(minc + 1, maxc):  # only a - c combs where a may be less than c
            dp[a] = 1 + min(dp[a - c] for c in coins if a - c >= 0)

        for a in range(maxc + 1, amount + 1):  # all a - c combs from here on are valid
            dp[a] = 1 + min(dp[a - c] for c in coins)
        return dp[-1] if dp[-1] != float("inf") else -1


# @lc code=end
