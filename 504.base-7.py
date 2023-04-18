#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
from collections import deque


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        res, sign = deque(), ''
        if num < 0:
            sign = '-'
            num = -num
        while num:
            res.appendleft(str(num % 7))
            num //= 7
        res.appendleft(sign)
        return ''.join(res)
# @lc code=end
