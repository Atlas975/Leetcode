#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
import numpy as np


class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = int(np.log10(num))
        while digits >= 0:
            if ((num // (10**digits)) % 10) == 6:
                return num + (3 * (10**digits))
            digits -= 1
        return num


# @lc code=end
