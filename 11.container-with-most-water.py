#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxarea = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                mxarea = max(mxarea, height[l] * (r - l))
                l += 1
            else:
                mxarea = max(mxarea, height[r] * (r - l))
                r -= 1
        return mxarea


# @lc code=end
