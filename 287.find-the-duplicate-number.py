#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slw, fst = nums[0], nums[nums[0]]
        while (slw != fst):
            slw, fst = nums[slw], nums[nums[fst]]

        slw2 = 0
        while (slw != slw2):
            slw, slw2 = nums[slw], nums[slw2]
        return slw


# @lc code=end
