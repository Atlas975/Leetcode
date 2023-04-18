#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#


# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def max_gap(size, cuts):
            cuts.sort()
            mxSize = max(cuts[0], size - cuts[-1])
            for i in range(1, len(cuts)):
                mxSize = max(mxSize, cuts[i] - cuts[i - 1])
            return mxSize

        return max_gap(h, horizontalCuts) * max_gap(w, verticalCuts)) % (10**9 + 7)


# @lc code=end
