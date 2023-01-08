#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        lprod = rprod = 1
        r = n - 1
        for l in range(n):
            res[l] *= lprod
            res[r - l] *= rprod
            lprod *= nums[l]
            rprod *= nums[r - l]

        return res


# @lc code=end
