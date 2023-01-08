#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        moves = set(range(1, maxChoosableInteger + 1))
        movesum = sum(moves)
        if desiredTotal <= maxChoosableInteger:
            return True
        if movesum < desiredTotal:
            return False
        while moves:
# @lc code=end

