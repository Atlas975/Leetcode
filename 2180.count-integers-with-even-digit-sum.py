#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
from functools import cache


class Solution:
    def countEven(self, num: int) -> int:
        @cache
        def sum_digits(num):
            return 0 if num == 0 else num % 10 + sum_digits(num // 10)

        return sum(sum_digits(i) % 2 == 0 for i in range(2, num + 1))


# @lc code=end
