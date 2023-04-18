#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
from collections import deque
from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry = deque(), 0
        for i, j in zip_longest(a[::-1], b[::-1], fillvalue=0):
            carry += int(i) + int(j)
            res.appendleft(carry % 2)
            carry //= 2
        if carry:
            res.appendleft(carry)
        return "".join(map(str, res))


# @lc code=end
