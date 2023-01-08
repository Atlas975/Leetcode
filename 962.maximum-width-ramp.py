#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l, n = 0, len(nums)
        l, r = 0, n - 1
        mxwidth = 0

        while l < r:
            if nums[l] > nums[r]:
                mxwidth = max(mxwidth, r - l)
                l += 1
            else:
                mxwidth = max(mxwidth, r - l)

                r -= 1

        return mxwidth


# @lc code=end
