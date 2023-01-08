#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next((k for k, v in Counter(nums).items() if v == 1), -1)


# @lc code=end
