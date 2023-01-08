#
# @lc app=leetcode id=805 lang=python3
#
# [805] Split Array With Same Average
#

# @lc code=start
from functools import lru_cache


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def solve(s: int, k: int, i: int) -> int:
            return 0

        n, s = len(nums), sum(nums)


# @lc code=end
