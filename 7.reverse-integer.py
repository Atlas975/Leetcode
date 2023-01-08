#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

from itertools import takewhile


class Solution:
    def reverse(self, x: int) -> int:
        s = 1 - 2 * (x < 0)
        x *= s
        r = 0
        while x > 0:
            r *= 10
            r += x % 10
            x //= 10
        return s * r * (r < 2**31)


# @lc code=end
