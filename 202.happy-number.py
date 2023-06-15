#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from functools import cache


class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            return n == 1 or n == 7

        def digit_sum(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res
        
        while n != 1 and n != 4:
            n = digit_sum(n)
        return n == 1


# @lc code=end
