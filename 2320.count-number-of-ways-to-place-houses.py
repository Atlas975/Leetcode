#
# @lc app=leetcode id=2320 lang=python3
#
# [2320] Count Number of Ways to Place Houses
#

# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n == 1:
            return 4
        if n == 2:
            return 9
        a, b = 2, 3
        for _ in range(3, n + 1):
            a, b = b, a + b
        return (b * b) % (10**9 + 7)


# @lc code=end
