#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
from math import sqrt, ceil


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        res = 1 + sum(i + num / i for i in range(2, ceil(sqrt(num))) if num % i == 0)
        return res == num


# @lc code=end
