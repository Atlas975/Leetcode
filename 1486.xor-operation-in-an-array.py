#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
from functools import reduce
from operator import xor


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(xor, (start + 2 * i for i in range(n)))
        # res=0
        # for i in range(n):
        #     res ^= start + 2*i
        # return res


# @lc code=end
