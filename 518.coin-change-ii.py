#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins = sorted((c for c in coins if c <= amount), reverse=True)
        coins = [c for c in coins if c <= amount]
        if len(coins) == 0:
            return 1 if amount == 0 else 0

        def backtrack
        
# @lc code=end

