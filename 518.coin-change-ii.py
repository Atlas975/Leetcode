#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins: # can only use each coin once (combination)
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        return dp[amount]


# @lc code=end
