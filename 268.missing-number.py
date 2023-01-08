#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from functools import reduce
from operator import xor


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) ^ reduce(xor, (i ^ n for i, n in enumerate(nums)))


# @lc code=end
