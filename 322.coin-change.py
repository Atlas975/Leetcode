#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins = [c for c in coins if c <= amount]
        if len(coins) == 0:  # no coins needed if amt = 0, no coins available if amt > 0
            return 0 if amount == 0 else -1
        n = max(coins) + 1
        dp = [float("inf")] * n

        dp[0], dp[n - 1] = 0, 1
        for c in coins:
            for a in range(c, n - 1):
                dp[a] = min(dp[a], 1 + dp[a - c])

        for a in range(n, amount + 1):  # all a - c combs from here on are valid
            dp[a % n] = 1 + min(dp[(a - c) % n] for c in coins)
        return dp[amount % n] if dp[amount % n] != float("inf") else -1


# @lc code=end
