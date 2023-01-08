#
# @lc app=leetcode id=2344 lang=python3
#
# [2344] Minimum Deletions to Make Array Divisible
#

# @lc code=start

from math import gcd


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:

        g = gcd(*numsDivide)
        mindiv = min((num for num in nums if g % num == 0), default=None)
        return sum(num < mindiv for num in nums) if mindiv else -1


# @lc code=end
