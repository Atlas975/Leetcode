#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# from math import log
# get numpy base log 4
import numpy as np


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # while n > 1:
        #     if n%4 > 0:
        #         return False
        #     n //=4
        # return n == 1
        return False if n <= 0 else np.log(n) / np.log(4) % 1 == 0


# @lc code=end
