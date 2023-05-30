#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        a = b = res = nums[0]  # a: min, b: max
        for num in nums[1:]:
            if num < 0:  # a can be max if num < 0 twice
                a, b = b, a
            a, b = min(num, a * num), max(num, b * num)
            res = max(res, b)
        return res


# @lc code=end
