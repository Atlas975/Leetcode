#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start


class Solution:
    def getSum(self, a: int, b: int) -> int:

        add = lambda a, b: add(a ^ b, (a & b) << 1) if b else a
        inv = lambda x: add(~x, 1)

        if a * b < 0:
            if a > 0:
                a, b = b, a
            ia = inv(a)
            if ia == b:
                return 0
            if ia < b:
                ib = inv(b)
                return inv(add(ia, ib))
        return add(a, b)


# @lc code=end
