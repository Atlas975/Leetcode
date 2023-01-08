#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slw, fst = nums[0], nums[0]
        while True:
            slw, fst = nums[slw], nums[nums[fst]]
            if slw == fst:
                break

        slw = nums[0]
        while slw != fst:
            slw, fst = nums[slw], nums[fst]

        return slw


# @lc code=end
