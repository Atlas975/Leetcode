#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from functools import cache


class Solution:
    def isHappy(self, n: int) -> bool:
        if n in {1, 7}:
            return True
        if n < 10:
            return False

        @cache
        def digit_sum(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res

        fst = digit_sum(n)
        while n not in {1, fst}:
            n = digit_sum(n)
            fst = digit_sum(digit_sum(fst))
        return n == 1


# @lc code=end
