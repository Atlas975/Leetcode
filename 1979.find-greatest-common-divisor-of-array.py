#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
from math import gcd


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))


# @lc code=end
