#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxar = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                mxar = max(mxar, height[l] * (r - l))
                l += 1
            else:
                mxar = max(mxar, height[r] * (r - l))
                r -= 1
        return mxar


# @lc code=end
